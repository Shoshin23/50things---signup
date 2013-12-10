from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from forms import SignupForm
from models import Signup

import base36


def home(request, code=None):
        form = SignupForm(request.POST or None)
        if request.method == 'POST':
                if form.is_valid():
                        signup = form.save()
                        request.session['code'] = base36.base36encode(signup.pk)

                        if code:
                                try:
                                        signup_inviter = Signup.objects.get(pk=base36.base36decode(code.upper()))
                                        signup_inviter.save()
                                except Exception, e:
                                        pass

                        return redirect(reverse('launch_app_success'))
                else:
                        try:
                                signup = Signup.objects.get(email=form.data.get('email', ''))
                                return render_to_response('launch/already_registered.html', context_instance=RequestContext(request))
                        except:
                                pass
        return render_to_response('launch/form.html', {'form': form},
                                  context_instance=RequestContext(request))


def success(request):
        return render_to_response('launch/success.html',
                                  context_instance=RequestContext(request))

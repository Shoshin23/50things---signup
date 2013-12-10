from django.db import models


class Signup(models.Model):
        added = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)

        email = models.EmailField("Your email:", unique=True)
        city = models.CharField("Your city:", max_length=100)
        invitation_sent = models.BooleanField(default=False)

        def __unicode__(self):
                return u"Signup <%s> for the city <%s>" % (self.email, self.city)

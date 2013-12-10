from django import forms

from models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        widgets = {
                'city': forms.TextInput (attrs={'placeholder': 'Enter your city...'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Enter your email...'}),
}
        exclude = ('invitation_sent', 'invitees',)

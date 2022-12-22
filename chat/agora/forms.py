from django import forms
from .models import user_registration
class user_form(forms.Form):
    user_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        models=user_registration

        field= '__all__'

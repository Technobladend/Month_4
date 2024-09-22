import email
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password = forms.CharField()
    password_confirm = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
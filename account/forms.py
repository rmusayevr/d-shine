from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Şifrələr eyni deyil!")
        return password2


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput())


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label='New Password',
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
                                    widget=forms.PasswordInput())

    def clean_new_password2(self):
        new_password1 = self.cleaned_data["new_password1"]
        new_password2 = self.cleaned_data["new_password2"]

        if new_password1 != new_password2:
            raise forms.ValidationError("Şifrələr eyni deyil!")
        return new_password2

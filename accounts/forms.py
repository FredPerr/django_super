from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class PasswordChange(PasswordChangeForm):
    pass


class PasswordResetForm(PasswordResetForm):
    pass


class PasswordResetConfirmForm(SetPasswordForm):
    pass
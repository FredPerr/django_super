from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model


INPUT_ATTRIBUTES = {'placeholder': ' ', 'class': 'input'}


class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=INPUT_ATTRIBUTES))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs=INPUT_ATTRIBUTES))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(INPUT_ATTRIBUTES, **{'autocomplete': 'new-password'})))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(INPUT_ATTRIBUTES, **{'autocomplete': 'new-password'})))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or username', widget=forms.TextInput(attrs=INPUT_ATTRIBUTES))
    password = forms.CharField(widget=forms.PasswordInput(attrs=INPUT_ATTRIBUTES))

    error_messages = {
        'invalid_login': "Please enter the correct %(username)s and password.",
        'inactive': "This account is inactive."
    }

class PasswordChange(PasswordChangeForm):
    pass


class PasswordResetForm(PasswordResetForm):
    pass


class PasswordResetConfirmForm(SetPasswordForm):
    pass
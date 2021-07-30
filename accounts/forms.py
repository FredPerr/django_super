from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model, password_validation


class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput())
    email = forms.CharField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or username', widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    error_messages = {
        'invalid_login': "Please enter the correct %(username)s and password.",
        'inactive': "This account is inactive."
    }

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label= "Old password", strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    error_messages = {
        'password_incorrect': "Your old password was entered incorrectly.",
    }


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
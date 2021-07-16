from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model, password_validation


INPUT_ATTRIBUTES = {'placeholder': ' '}


class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs=INPUT_ATTRIBUTES))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs=INPUT_ATTRIBUTES))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}))

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

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label= "Old password", strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, **INPUT_ATTRIBUTES}),
    )
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}),
    )
    error_messages = {
        'password_incorrect': "Your old password was entered incorrectly.",
    }


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', **INPUT_ATTRIBUTES})
    )


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label= "New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label= "New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', **INPUT_ATTRIBUTES}),
    )
from django.forms import ModelForm, Form, EmailField
from django.urls import reverse_lazy
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import (
    UserCreationForm, 
    AuthenticationForm,PasswordChangeForm, 
    PasswordResetForm, SetPasswordForm
)

from .models import User


class EmailTestForm(Form):
    email = EmailField()


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            '<a class="underline" href="{}">this form</a>.',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format(reverse_lazy('password:change'))
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )

class UserConnectForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email',)


class UserRecoverForm(PasswordResetForm):
    pass
    

class UserPasswordChangeForm(PasswordChangeForm):
    pass


class UserPasswordSetForm(SetPasswordForm):
    pass
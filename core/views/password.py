from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.views import (
    PasswordChangeView, PasswordResetView,
    PasswordChangeDoneView as PCD,
    PasswordResetConfirmView
)

from ..forms import (
    UserPasswordChangeForm, UserRecoverForm,
    UserPasswordSetForm
)


class PasswordEditView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password:change-done")
    template_name = "core/auth/password/change.html"
    title = "Password change"


class PasswordRecoverView(PasswordResetView):
    email_template_name = "core/auth/password/reset-email.html"
    form_class = UserRecoverForm
    subject_template_name = "core/auth/password/reset-email-subject.txt"
    success_url = reverse_lazy("password:recover-done")
    template_name = "core/auth/password/recover.html"


class PasswordResetView(PasswordResetConfirmView):
    form_class = UserPasswordSetForm
    success_url = reverse_lazy("password:recover-complete")
    template_name = "core/auth/password/reset.html"


class PasswordChangeDone(PCD):
    template_name = "core/auth/password/change-done.html"

    
def password_recover_done(request):
    return render(request, 'core/auth/password/recover-done.html')


def password_reset_complete(request):
    return render(request, 'core/auth/password/reset-complete.html')
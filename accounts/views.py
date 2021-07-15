from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Account
from .forms import LoginForm, PasswordResetConfirmForm, RegisterForm, PasswordChangeForm, PasswordResetForm


EXTRA_CONTEXT = {
    'scss_path': 'accounts/style/accounts.scss',
    'ts_path': 'accounts/script/accounts.ts'
}


class RegisterView(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    extra_context = EXTRA_CONTEXT


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    extra_context = EXTRA_CONTEXT


class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    extra_context = EXTRA_CONTEXT


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'accounts/password/password-change.html'
    success_url = reverse_lazy('accounts:password-change-done')
    form_class = PasswordChangeForm
    extra_context = EXTRA_CONTEXT


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'accounts/password/password-change-done.html'
    extra_context = EXTRA_CONTEXT


class PasswordResetView(views.PasswordResetView):
    template_name = 'accounts/password/password-reset.html'
    success_url = reverse_lazy('accounts:password-reset-done')
    email_template_name = 'accounts/password/password-reset-email.html'
    subject_template_name = 'accounts/password/password-reset-subject.txt'
    form_class = PasswordResetForm
    extra_context = EXTRA_CONTEXT


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'accounts/password/password-reset-done.html'
    extra_context = EXTRA_CONTEXT


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'accounts/password/password-reset-confirm.html'
    success_url = reverse_lazy('accounts:password-reset-complete')
    form_class = PasswordResetConfirmForm
    extra_context = EXTRA_CONTEXT


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'accounts/password/password-reset-complete.html'
    extra_context = EXTRA_CONTEXT


@login_required
def details(request, username=''):

    if username == '':
        return render(request, 'accounts/details.html', context={'user': request.user})
    
    try:
        user = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return render(request, 'accounts/details.html', context={'username': username})
    return render(request, 'accounts/details.html', context={'user': user})
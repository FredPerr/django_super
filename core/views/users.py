from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views

from ..forms import UserRegisterForm, UserConnectForm
from ..urls import HOME_URL


class RegisterView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy(HOME_URL)
    template_name = "core/users/auth/register.html"


class LoginView(views.LoginView):
    form_class = UserConnectForm
    success_url = reverse_lazy(HOME_URL)
    template_name = "core/users/auth/login.html"
    redirect_authenticated_user = True


class LogoutView(views.LogoutView):
    template_name = "core/users/auth/logout.html"
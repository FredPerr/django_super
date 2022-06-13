from django.urls import path


from ..views.auth import RegisterView, LoginView, LogoutView


app_name = 'auth'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
from django.urls import path


from ..views.users import RegisterView, LoginView, LogoutView


app_name = 'auth'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='logout'),
]
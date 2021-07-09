from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('', views.details, name='details'),
    path('details/<username>/', views.details, name='details'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password-change', views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change-done', views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset/complete', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]
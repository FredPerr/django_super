from django.urls import path


from ..views.password import (
    PasswordEditView, PasswordChangeDone, PasswordRecoverView, 
    password_recover_done, PasswordResetView, password_reset_complete
)


app_name = 'password'


urlpatterns = [
    path('change/', PasswordEditView.as_view(), name='change'),
    path('change/done/', PasswordChangeDone.as_view(), name='change-done'),
    path('recover/', PasswordRecoverView.as_view(), name='recover'),
    path('recover/done/', password_recover_done, name='recover-done'),
    path('reset/<uidb64>/<token>/', PasswordResetView.as_view(), name='reset'),
    path('recover/completed/', password_reset_complete, name='recover-complete'),
]
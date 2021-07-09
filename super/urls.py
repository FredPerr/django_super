from django.urls import path

from .views import home


app_name = 'super'


urlpatterns = [
    path('', home, name='home')
]
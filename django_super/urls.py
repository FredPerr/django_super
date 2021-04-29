from django.contrib import admin
from django.urls import path
from super import views as super_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', super_views.home, name='home')
]

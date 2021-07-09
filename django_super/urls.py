from django.contrib import admin
from django.urls import path, include
from super import views as super_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('super.urls')),
    path('accounts/', include('accounts.urls')), # @OVERRIDE
]

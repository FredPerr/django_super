from django.urls import path, include


from ..views.core import home

urlpatterns = [

    path('', home, name='home'),

    path('auth/', include('core.urls.auth')),
    path('password/', include('core.urls.password')),
]
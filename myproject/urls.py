# urls.py en myproject

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', lambda request: redirect('login')),  # Redirige a la página de inicio de sesión
]



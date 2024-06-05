from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('buscar/', views.search_view, name='buscar'),
    path('listar/', views.listar_view, name='listar'),
    path('detalle/<int:pk>/', views.detalle_view, name='detalle'),
    path('editar/<int:pk>/', views.editar_view, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_view, name='eliminar'),
    path('listar_usuarios/', views.listar_usuarios_view, name='listar_usuarios'),
    path('registrar_usuario/', views.registrar_usuario_view, name='registrar_usuario'),
    path('editar_usuario/<int:pk>/', views.editar_usuario_view, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', views.eliminar_usuario_view, name='eliminar_usuario'),
]




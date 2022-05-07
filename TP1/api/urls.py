from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('', views.home, name="Forum"),
    path('forum/', views.home, name="Forum"),
    path('registro/', views.formDeRegistro,name="Registro"),
    path('login/', views.formDeLogin,name="Login"),
    path('logout', views.formDeLogout, name="Logout"),
    path('perfil/', views.perfil, name="Perfil")
]

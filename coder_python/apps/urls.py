from django.urls import path
from apps import views

urlpatterns = [
    path('', views.inicio, name="index"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('cliente/', views.cliente, name="cliente"),
    path('producto/', views.productos, name="productos"),
]
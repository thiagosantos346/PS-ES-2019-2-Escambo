from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'perfil'

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('sair', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
	path('board', views.dashBoard, name='borad'),
	path('register', views.register, name='register'),
]
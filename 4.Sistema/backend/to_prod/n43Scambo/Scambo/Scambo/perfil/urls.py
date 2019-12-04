from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'perfil'

urlpatterns = [
	path('', auth_views.LoginView.as_view(template_name='login.html')),
	path('board', views.dashBoard),
	path('register', views.register),
]
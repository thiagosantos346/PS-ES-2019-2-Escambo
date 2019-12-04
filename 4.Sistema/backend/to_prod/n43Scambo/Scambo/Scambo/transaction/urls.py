from django.urls import path
from .views import register

app_name = 'perfil'

urlpatterns = [
   path('', register , name='register' )
]


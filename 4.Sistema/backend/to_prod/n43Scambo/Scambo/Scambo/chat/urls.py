from django.urls import path
from .views import register

app_name = 'chat'

urlpatterns = [
   path('', register , name='home' )
]


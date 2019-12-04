from django.urls import path
from .views import register

app_name = 'catalog'

urlpatterns = [
   path('', register , name='home' )
]


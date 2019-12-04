from django.urls import path
from .views import register

app_name = 'score'

urlpatterns = [
   path('', register , name='home' )
]


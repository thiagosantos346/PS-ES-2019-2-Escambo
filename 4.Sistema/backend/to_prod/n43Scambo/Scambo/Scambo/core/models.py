from django.db import models
from django.conf import settings

class HomePage(models.Model):
   wellcome =  models.CharField(max_length=100)
   last_update = models.DateTimeField(auto_now_add=True)

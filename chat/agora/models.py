from django.db import models

# Create your models here.
class user_registration(models.Model):
    user_name=models.CharField(max_length=70)
    user_password=models.CharField(max_length=70)
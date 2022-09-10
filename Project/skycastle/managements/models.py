from django.db import models

# Create your models here.

class Users_kakao(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=200)
    user_id = models.CharField(max_length=500)
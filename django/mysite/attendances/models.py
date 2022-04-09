from django.db import models

# Create your models here.
class Attendance(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

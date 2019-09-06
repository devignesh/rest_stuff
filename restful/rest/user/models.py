from django.db import models

# Create your models here.

class User(models.Model):
    msg = models.CharField(max_length=50)

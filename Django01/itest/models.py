from django.db import models

# Create your models here.


class users(models.Model):
    name = models.CharField(max_length=20)
    passward = models.CharField(max_length=30)

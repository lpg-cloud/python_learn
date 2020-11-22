import channels
from django.db import models
from django.db.models.base import Model


# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=20)


class clients(models.Model):
    channel_name = models.CharField(max_length=40)
    user_name = models.models.OneToOneField(user, on_delete=models.DO_NOTHING)(user,on_delete=models.deletion)

import channels
from django.db import models
from django.db.models.base import Model

# Create your models here.

class user(models.Model):
  name=models.CharField(max_length=20)
  gender_choise=[('F','男'),('M','女')]
  gender=models.CharField(max_length=2,choices=gender_choise,default='F')
  tel_number=models.CharField(max_length=11)
  address=models.CharField(max_length=50)
  icon=models.BinaryField()

class clients(models.Model):
  channel_name=models.CharField(max_length=40)
  user_name=models.OneToOneField(to= user, on_delete=models.CASCADE)
  login_time=models.DateTimeField('date_login')

class group(models.Model):
  name=models.CharField(max_length=20)
  icon=models.BinaryField()

class user_group(models.Model):
  user_id=models.OneToOneField(user, on_delete=models.CASCADE)
  group_id=models.OneToOneField(group, on_delete=models.CASCADE)
  is_owner=models.BooleanField(default=False)
  is_manager=models.BooleanField(default=False)


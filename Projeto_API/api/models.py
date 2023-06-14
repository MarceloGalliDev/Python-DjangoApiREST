from django.db import models


class Company(models.Model):
  name=models.CharField(max_length=50)
  website=models.URLField(max_length=100)
  foundation=models.PositiveIntegerField()
  
  
class Programmer(models.Model):
  fullname=models.CharField(max_length=100)
  nickname=models.CharField(max_length=50)
  age=models.PositiveIntegerField()
  is_active=models.BooleanField(default=True)
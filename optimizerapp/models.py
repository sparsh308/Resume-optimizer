from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Developer_info(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class UserProfile(models.Model):

    function=models.CharField(max_length=100)
    salarybkt=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    doc=models.FileField(upload_to='Appdata')
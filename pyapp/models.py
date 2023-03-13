from django.db import models

# Create your models here.
class studentdb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)
    phone=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="profile", null=True, blank=True)
class catdb(models.Model):
    catname = models.CharField(max_length=30, null=True, blank=True)
    catdis=models.CharField(max_length=30, null=True, blank=True)
    catimg=models.ImageField(upload_to="profile", null=True, blank=True)
class productdb(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    price=models.CharField(max_length=30,null=True,blank=True)
    quantity= models.IntegerField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)
    category=models.CharField(max_length=30,null=True,blank=True)


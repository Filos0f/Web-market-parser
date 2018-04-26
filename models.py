
# coding: utf-8

from django.db import models

# Create your models here.

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	
	name = models.CharField(max_length=128, default="")
	desc = models.TextField(default="")
	type = models.CharField(max_length=64, default="")
	cost = models.IntegerField(default=0)
	img = models.CharField(max_length=256, default="")
	link = models.CharField(max_length=256, default="")
	market = models.CharField(max_length=64, default="")
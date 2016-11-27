from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)


class Producer(models.Model):
    title = models.CharField(max_length=200)
    country_code = models.CharField(max_length=2)


class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.IntegerField()
    category = models.ForeignKey(Category)
    producer = models.ForeignKey(Producer)

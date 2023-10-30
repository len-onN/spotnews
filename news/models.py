# ecommerce/products/models.py

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    pass


class News(models.Model):
    pass
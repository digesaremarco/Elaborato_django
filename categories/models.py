from django.db import models

# Create your models here.
class Category(models.Model):
    description = models.TextField(max_length=200)
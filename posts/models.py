from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categorie = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
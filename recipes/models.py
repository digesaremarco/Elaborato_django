from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
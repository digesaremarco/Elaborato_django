# Generated by Django 4.2.1 on 2023-05-31 10:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0009_alter_recipe_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorites',
        ),
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
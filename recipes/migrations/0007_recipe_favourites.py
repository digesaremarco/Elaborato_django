# Generated by Django 4.2.1 on 2023-05-30 21:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0006_recipe_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
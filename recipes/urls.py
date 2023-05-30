from django.urls import path
from .views import AllRecipes, UpdateRecipe

urlpatterns = [
    path("", AllRecipes, name="home"),
    path('update/<int:recipe_id>/', UpdateRecipe, name='update_recipe'),
]
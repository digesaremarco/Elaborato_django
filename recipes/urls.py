from django.urls import path
from .views import AllRecipes, UpdateRecipe, NewRecipe

urlpatterns = [
    path("", AllRecipes, name="home"),
    path('update/<int:recipe_id>/', UpdateRecipe, name='update_recipe'),
    path('create/', NewRecipe, name='create_recipe')
]
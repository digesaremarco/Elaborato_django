from django.urls import path
from .views import AllRecipes, UpdateRecipe, NewRecipe, MyRecipes

urlpatterns = [
    path("", AllRecipes, name="home"),
    path('update/<int:recipe_id>/', UpdateRecipe, name='update_recipe'),
    path('create/', NewRecipe, name='create_recipe'),
    path('my_recipes/', MyRecipes, name='my_recipes')
]
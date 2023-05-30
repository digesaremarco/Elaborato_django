from django.urls import path
from .views import AllRecipes, UpdateRecipe, NewRecipe, MyRecipes, DeleteRecipe, ViewRecipe

urlpatterns = [
    path("", AllRecipes, name="home"),
    path('update/<int:recipe_id>/', UpdateRecipe, name='update_recipe'),
    path('create/', NewRecipe, name='create_recipe'),
    path('my_recipes/', MyRecipes, name='my_recipes'),
    path('delete/<int:recipe_id>/', DeleteRecipe, name='delete_recipe'),
    path('view/<int:recipe_id>/', ViewRecipe, name='view_recipe'),
]
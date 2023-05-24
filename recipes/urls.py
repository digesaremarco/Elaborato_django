from django.urls import path
from .views import RecipeCreateView, RecipeDeleteView, RecipeDetailView, RecipeListView, RecipeUpdateView

urlpatterns = [
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("", RecipeListView.as_view(), name="recipe_list"),
]
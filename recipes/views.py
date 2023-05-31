from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RecipeForm
from .models import Recipe


def AllRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


@login_required
def NewRecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


@login_required
def UpdateRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'update_recipe.html', {'form': form})


@login_required
def MyRecipes(request):
    my_recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'my_recipes.html', {'my_recipes': my_recipes})


@login_required
def DeleteRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    return render(request, 'delete_recipe.html', {'recipe': recipe})


def ViewRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'view_recipe.html', {'recipe': recipe})


def AddFavorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    request.user.favorite.add(recipe)
    return redirect('view_recipe', recipe_id=recipe_id)


def RemoveFavorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    request.user.favorite.remove(recipe)
    return redirect('view_recipe', recipe_id=recipe_id)
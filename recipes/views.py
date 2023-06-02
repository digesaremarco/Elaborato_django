from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect

from .forms import RecipeForm
from .models import Recipe


def AllRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


@login_required
@csrf_protect
def NewRecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()

    return render(request, 'create_recipe.html', {'form': form})


@login_required
@csrf_protect
def UpdateRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES, instance=recipe)
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
@csrf_protect
def DeleteRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == 'POST':
        recipe.delete()
        return redirect('home')

    return render(request, 'delete_recipe.html', {'recipe': recipe})


def ViewRecipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'view_recipe.html', {'recipe': recipe})


@login_required
def AddFavorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    request.user.favorite.add(recipe)
    return redirect('view_recipe', recipe_id=recipe_id)


@login_required
def RemoveFavorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    request.user.favorite.remove(recipe)
    return redirect('view_recipe', recipe_id=recipe_id)


@login_required
def ViewFavorites(request):
    favorite_recipe = request.user.favorite.all()
    return render(request, 'view_favorites.html', {'recipe': favorite_recipe})

def SearchRecipe(request):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(title__icontains=query)
    return render(request, 'search_recipes.html', {'recipes': recipes, 'query': query})

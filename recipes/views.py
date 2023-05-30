from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RecipeForm
from .models import Recipe

def AllRecipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

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
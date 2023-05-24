from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Recipe

# Create your views here.

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_new.html'
    fields = ('title', 'description', 'category')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_list')

    def test_func(self): #function that checks if the user who wants to delete the recipe is the author
        obj = self.get_object()
        return obj.author == self.request.user

class RecipeUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Recipe
    template_name = 'recipe_edit.html'
    fields = ('title', 'description', 'category')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class RecipeDetailView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeListView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'recipe_list.html'
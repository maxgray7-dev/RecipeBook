from django.shortcuts import render
from django.contrib import messages
from .forms import NewRecipeForm






# Create your views here.

def new_recipe(request):
    return render(request, 'new_recipe/new_recipe.html')



from django.shortcuts import render
from django.views import generic
from .models import Recipe
from django.shortcuts import get_object_or_404







# Create your views here.

# Main View that displays all recipes on the Home Page



class RecipeList(generic.ListView):
    
    # The code below will displays only objects that have status "published"
    queryset = Recipe.objects.all()

    template_name = 'recipe_app/index.html'
    paginate_by = 9
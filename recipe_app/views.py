from django.shortcuts import render
from django.views import generic
from .models import Recipe
from django.shortcuts import get_object_or_404







# Create your views here.

# Main View that displays all recipes on the Home Page



class RecipeList(generic.ListView):
    
    # The code below will displays only objects that have status "published"
    queryset = Recipe.objects.filter(status=1)

    template_name = 'recipe_app/index.html'
    paginate_by = 9



def recipe_detail(request, slug):
    
    #Display an individual :model:'blog.Post'.
    
    #   ***Context***
    #   'post''
    #   An instance of :model:'blog.Post'.

    #   *** Template ***
    #   :template:'blog/post_detail.html'
    queryset = Recipe.objects.filter()
    recipe = get_object_or_404(queryset, slug=slug)

    print("About to render template")

    return render(
        request,
        "recipe_app/recipe_detail.html",
        {"r": recipe,
        },

    )

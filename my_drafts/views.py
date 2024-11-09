from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views import generic
from recipe_app.models import Recipe
from django.shortcuts import get_object_or_404







# Create your views here.

# Main View that displays all recipes on the Home Page



class RecipeEditList(generic.ListView):
    
    # The code below will displays only objects that have status "published"
    def get_queryset(self):
        return Recipe.objects.filter(status=0, author=self.request.user)

    template_name = 'my_drafts/my_drafts.html'
    paginate_by = 9


def recipe_delete(request, slug):
    """
    view to delete recipe
    """
    queryset = Recipe.objects.filter(status=0)
    recipe = get_object_or_404(queryset, slug=slug)
    recipe.delete()

    return HttpResponseRedirect(reverse('my_drafts:my_drafts'))
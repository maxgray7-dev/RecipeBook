from django.shortcuts import render
from django.views import generic
from .models import Recipe
from django.http import HttpResponseRedirect







# Create your views here.

# Main View that displays all recipes on the Home Page

class RecipeBook(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = 'recipe_app/index.html'
    paginate_by = 5


def recipes_detail(request, title):
    queryset = Recipe.objects.filter(status=1)
    post=get_object_or_404(queryset, title=title)



    return render(
        request, recipe_app/'recipes_detail.html',
  
)
from django.shortcuts import render, redirect
from .forms import RecipeForm
from recipe_app.models import Recipe



# Create your views here.

def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.author = request.user
            saved_form.save()
            return redirect("recipe_success")
    else:
        form = RecipeForm()
    return render(request, 'new_recipe/new_recipe.html', {'form': form})


def recipe_success(request):
    return render(request, 'new_recipe/recipe_success.html')


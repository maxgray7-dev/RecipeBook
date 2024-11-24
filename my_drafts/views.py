from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.views import generic
from recipe_app.models import Recipe
from django.shortcuts import get_object_or_404
from .forms import RecipeForm
import logging
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)







# Create your views here.

# Main View that displays all recipes on the Home Page



class RecipeEditList(generic.ListView):
    
    # The code below will displays only objects that have status "published"
    def get_queryset(self):
        return Recipe.objects.filter(status=0, author=self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        formset = {}
        for query in queryset:
            obj = get_object_or_404(queryset, slug=query.slug)
            # recipe = get_object_or_404(queryset, slug=slug)
            formset[query.slug] = RecipeForm(instance=obj)
            # formset[query.slug].instance.description.widget = SummernoteWidget()
        logger.info('forms dict: %s', formset)
        for slug, f in formset.items():
            logger.info('form %s\n%s\n', f.instance.title, f.instance.description)
        data['forms'] = formset
        return data

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


#  Editing Recipe 

def recipe_edit(request, slug):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.author = request.user

            if form.cleaned_data['featured_image'] == 'placeholder':
                queryset = Recipe.objects.filter(status=0)
                recipe = get_object_or_404(queryset, slug=slug)
                saved_form.featured_image = recipe.featured_image

            Recipe.objects.filter(slug=slug).delete()
            
            saved_form.save()
            return redirect("my_drafts:recipe_success")
    else:
        queryset = Recipe.objects.filter(status=0)
        recipe = get_object_or_404(queryset, slug=slug)
        form = RecipeForm(initial={'title': recipe.title, 'description': recipe.description})

    return render(request, 'my_drafts/edit_recipe.html', {'form': form})

# Show to user that new recipe has been added succesfully
def recipe_success(request):
    return render(request, 'my_drafts/recipe_success.html')
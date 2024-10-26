from django import forms
from recipe_app.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'author', 'featured_image',)
        

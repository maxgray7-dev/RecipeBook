from django import forms
from recipe_app.models import Recipe
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'featured_image',)
    description = forms.CharField(widget=SummernoteWidget())
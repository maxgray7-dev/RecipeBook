from .models import NewRecipeRequest
from django import forms


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = NewRecipeRequest
        fields = ('title', 'description', 'author', 'featured_image',)
        

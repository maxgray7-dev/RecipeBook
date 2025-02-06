

from django.test import TestCase
from .forms import RecipeForm


class TestRecipeForm(TestCase):

    def test_form_is_valid(self):
        recipe_form = RecipeForm({'title': 'Recipe', 'description': 'Delicious doughnut', 'featured_image': 'picture is coming'})
        self.assertTrue(recipe_form.is_valid())


from django.test import TestCase
from .forms import RecipeForm


class TestRecipeForm(TestCase):

    def test_form_is_valid(self):
        recipe_form = RecipeForm({'title': 'Recipe', 'description': 'Delicious doughnut', 'featured_image': 'picture is coming'})
        self.assertTrue(recipe_form.is_valid())


    def test_form_is_invalid(self):
        recipe_form = RecipeForm({'title': 'Recipe', 'test': 'Delicious doughnut'})
        self.assertFalse(recipe_form.is_valid())

   #Testing each field# 
    
    def test_title_is_required(self):
        """Test for the 'title' field"""
        form = RecipeForm({'description': 'Delicious doughnut', 'featured_image': 'picture is coming'})
        self.assertFalse(
            form.is_valid(),
            msg="Title was not provided, but the form is valid"
        )

   
    def test_description_is_required(self):
        """Test for the 'description' field"""
        form = RecipeForm({'title': 'Recipe', 'featured_image': 'picture is coming'})
        self.assertFalse(
            form.is_valid(),
            msg="Description was not provided, but the form is valid"
        )

    def test_featured_image_is_optional(self):
        """Test for the 'featured_image' field"""
        form = RecipeForm({'title': 'Recipe', 'description': 'Delicious doughnut' })
        self.assertTrue(
            form.is_valid(),
            msg="Optional image was not provided, but the form is invalid"
        )
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class TestRecipeViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        recipe_data = {'title': 'Recipe', 'description': 'Delicious doughnut', 'featured_image': 'picture is coming'}
        response = self.client.post(reverse(
            'new_recipe'), recipe_data)
        print(response)
        # Asserted that we were redirected to a success page after a recipe creation
        # 302 is a code for redirection
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/recipe/success/")
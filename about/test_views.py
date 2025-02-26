from django.test import TestCase

class TestRecipeViews(TestCase):

    def test_render_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.content)

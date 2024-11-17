from . import views
from django.urls import path

app_name = 'my_drafts'


urlpatterns = [
    path('', views.RecipeEditList.as_view(), name='my_drafts'),
    path('edit_recipe/<slug:slug>', views.recipe_edit, name='edit_recipe'),
    path('delete_recipe/<slug:slug>', views.recipe_delete, name='delete_recipe'),
]
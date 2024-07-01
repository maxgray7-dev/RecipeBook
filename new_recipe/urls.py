from django.urls import path
from . import views


urlpatterns = [
    path('', views.new_recipe, name='new_recipe'),
    path('success/', views.recipe_success, name='recipe_success'),
]
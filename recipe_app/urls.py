from . import views
from django.urls import path

app_name = 'recipe_app'



urlpatterns = [
    path('', views.RecipeList.as_view(), name ='home'),
    path('detail/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]
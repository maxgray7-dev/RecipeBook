from django.urls import path
from . import views







urlpatterns = [
    path('', views.RecipeBook.as_view(), name ='home'),
    path('<title:title>', views.recipes_detail, name='recipes_detail'),
]
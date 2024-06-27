from django.urls import path
from . import views







urlpatterns = [
    path('', views.home, name="recipe_app-home"),
]
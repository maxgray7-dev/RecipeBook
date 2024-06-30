from . import views
from django.urls import path


urlpatterns = [
    path('', views.new_recipe, name='new_recipe'),
]
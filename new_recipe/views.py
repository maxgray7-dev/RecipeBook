from django.shortcuts import render
from django.contrib import messages
from .models import MyPage




# Create your views here.

def new_recipe(request):
    return render(request, 'new_recipe/new_recipe.html')



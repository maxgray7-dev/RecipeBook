from django.shortcuts import render
from django.http import HttpResponse







# Create your views here.
def home (request):
    return HttpResponse('<h1>Welcome to the Recipe Book</h1>')


def home(request):
  context = {
    'recipe_app': recipe_app
  }
  return render(request, 'recipe_app/home.html', context)
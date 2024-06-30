from django.shortcuts import render
from django.contrib import messages





# Create your views here.

def about(request):
    return render(request, 'about/about.html')



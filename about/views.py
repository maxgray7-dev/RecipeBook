from django.shortcuts import render
from django.contrib import messages
from .models import MyPage




# Create your views here.

def about_user(request):
    return render(request, 'about/about.html')



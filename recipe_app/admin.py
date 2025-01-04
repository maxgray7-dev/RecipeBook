from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe
from . import models




#Register your models here

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on', 'author', )
    search_fields = ['title', 'content']
    list_filter = ('author', 'title', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}





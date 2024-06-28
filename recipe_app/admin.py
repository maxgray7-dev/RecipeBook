from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe
from . import models




@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)





#Register your models here

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment
from . import models




@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    summernote_fields = ('content',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Comment)

#Register your models here

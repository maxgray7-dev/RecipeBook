from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment
from . import models




#Register your models here

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on', 'author', )
    search_fields = ['title', 'content']
    list_filter = ('author', 'title', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('author','post', 'created_on',)
    search_fields = ['athor', 'title']
    list_filter = ('author', 'post', 'created_on',)

# admin.site.register(Comment)



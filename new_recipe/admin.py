from django.contrib import admin
from .models import NewRecipeRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(NewRecipeRequest)
class NewRecipeRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'name',)

from django.contrib import admin
from django.db import models
from .models import Lesson, Tag, Image
from pagedown.widgets import AdminPagedownWidget
# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('author', 'title' , 'created_time')
    search_fields = ['title']
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ['description']

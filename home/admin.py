from django.contrib import admin
from django.db import models
from .models import Lesson, Tag
from pagedown.widgets import AdminPagedownWidget
# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('author', 'title' , 'content', 'created_time')
    search_fields = ['title']
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

from django.contrib import admin
from .models import Lesson, Tag
# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('author', 'title' , 'content', 'created_time')
    search_fields = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

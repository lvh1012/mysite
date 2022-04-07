from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve
from .models import Lesson
from django.http import Http404
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def learning(request):
    context = {'lessons': Lesson.objects.all().order_by('-created_time')}
    return render(request, 'pages/learning.html', context)

def lesson(request, id):
    context = {
        "current_url":  settings.DOMAIN + resolve(request.path_info).url_name
    }
    try:
        context["lesson"] = Lesson.objects.get(id=id)
    except Lesson.DoesNotExist:
        raise Http404("Bài viết không tồn tại")

    return render(request, 'pages/lesson.html', context)

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})
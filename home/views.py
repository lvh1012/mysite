from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def learning(request):
    return render(request, 'pages/learning.html')

def leeson(request):
    current_url = resolve(request.path_info).url_name
    return render(request, 'pages/leeson.html', {"current_url": current_url})

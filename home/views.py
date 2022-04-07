from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def learning(request):
    return render(request, 'pages/learning.html')

def leeson(request):
    return render(request, 'pages/leeson.html')

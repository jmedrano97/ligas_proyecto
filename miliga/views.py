from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'miliga/home.html')

def index(request):
    return render(request, 'miliga/index.html')

def equipos(request):
    return render(request, 'miliga/equipos.html')
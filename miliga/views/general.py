import os
from django.shortcuts import render

from ligas import settings
from miliga.models import *
from miliga.forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
import pandas as pd
from django.db.models import Count
from django.http import HttpResponse
import openpyxl


# Create your views here.

def home(request):
    return redirect('miliga:equipos')  

def index(request):
    context = {}
    context['zona'] = 'index'
    return render(request, 'miliga/index.html',context)

def matches(request):
    context = {}
    context['zona'] = 'matches'
    return render(request, 'miliga/proximamente.html',context)

def download_template(request, equipo_id=0):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    filepath = os.path.join(settings.BASE_DIR, 'media/archivos/formato.xlsx')
    workbook = openpyxl.load_workbook(filepath)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="plantilla_%s.xlsx"'%equipo.nombre
    workbook.save(response)
    
    return response

def download_ejemplo(request, equipo_id=0):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    filepath = os.path.join(settings.BASE_DIR, 'media/archivos/formato_ejemplo.xlsx')
    workbook = openpyxl.load_workbook(filepath)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="plantilla_de_ejemplo.xlsx"'
    workbook.save(response)
    
    return response
import os
import itertools
import random
import datetime
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
from django.db.models import Q, Prefetch
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError

# Create your views here.

def home(request):
    return redirect('miliga:equipos')  

def index(request):
    context = {}
    context['zona'] = 'index'
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/index.html',context)

def registrarse(request):
    context = {}
    context['vista'] = 'Registrarse'

    if request.method == 'GET':
        context['form'] = UserCreationForm()
        return render(request, 'miliga/registrarse.html', context)
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('miliga:index')
            except IntegrityError:
                mensaje = {'desc':'El usuario ya existe', 'tipo':'danger'}
                request.session['mensaje'] = mensaje
        mensaje = {'desc':'Error al confirmar resultado', 'tipo':'danger'}
        request.session['mensaje'] = mensaje
        context = comprobar_mensajes(request, context)
        return render(request, 'miliga/registrarse.html', context)

def salir(request):
        logout(request)
        return redirect('miliga:index')

def iniciar_sesion(request):
    context = {}
    context['vista'] = 'Iniciar Sesión'

    if request.method == 'GET':
        context['form'] = AuthenticationForm()
        return render(request, 'miliga/registrarse.html', context)
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            mensaje = {'desc':'Usuario o contraseña incorrectos', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            context = comprobar_mensajes(request, context)
            return render(request, 'miliga/registrarse.html', context)
        else:
            login(request, user)
            return redirect('miliga:index')


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

def comprobar_mensajes(request, context):
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return context
import os
from django.shortcuts import render
from datetime import datetime

from ligas import settings
from .models import *
from .forms import *
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


def equipos(request):
    context = {}
    context['zona'] = 'equipos'

    equipos = Equipo.objects.all().order_by('-id')
    context['equipos'] = equipos
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/equipos/equipos.html', context)

def create_equipo(request):
    context = {}
    context['zona'] = 'equipos'

    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('miliga:equipos')
    else:
        form = EquipoForm()
    
    context['form'] = form
    return render(request, 'miliga/equipos/create_equipo.html', context)

def detail_equipo(request, equipo_id):
    context = {}
    context['zona'] = 'equipos'

    equipo = get_object_or_404(Equipo, pk=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo_id)
    context['equipo'] = equipo
    context['jugadores'] = jugadores
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/equipos/detail_equipo.html', context)

def edit_equipo(request, equipo_id):
    context = {}
    context['zona'] = 'equipos'

    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            mensaje = {'desc':'El Equipo se ha editado correctamente', 'tipo':'success'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:detail_equipo', equipo_id=equipo.id)
        else:
            mensaje = {'desc':'Vaya! ha ocurrido un error al editar el equipo', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:edit_equipo', equipo_id=equipo.id)
    else:
        form = EquipoForm(instance=equipo)
    
    context['form'] = form
    context['equipo'] = equipo
    return render(request, 'miliga/equipos/edit_equipo.html', context)

def delete_equipo(request, equipo_id):
    context = {}
    try:
        equipo = get_object_or_404(Equipo, pk=equipo_id)
        equipo.delete()
        mensaje = {'desc':'El Equipo se ha eliminado correctamente', 'tipo':'success'}
    except:
        mensaje = {'desc':'Error al intentar eliminar Equipo', 'tipo':'danger'}

    request.session['mensaje'] = mensaje
    return redirect('miliga:equipos')



def jugadores(request):
    context = {}
    context['zona'] = 'jugadores'

    jugadores = Jugador.objects.all().order_by('-equipo')
    equipos = Equipo.objects.prefetch_related('jugador_set').annotate(num_jugadores=Count('jugador')).order_by('-num_jugadores')
    context['jugadores'] = jugadores
    context['equipos'] = equipos
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/jugadores/jugadores.html', context)



def create_jugador(request,equipo_id=0):
    context = {}
    context['zona'] = 'jugadores'

    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        print('CRATE______')
        if form.is_valid():
            print('VALIDO______')
            form.save()
            mensaje = {'desc':'El Jugador se ha agregado correctamente', 'tipo':'success'}
            request.session['mensaje'] = mensaje
            print('REDIRECT______')
            print('equipo_id______', equipo_id)
            return redirect('miliga:detail_equipo', equipo_id=equipo_id)
        else:
            mensaje = {'desc':'Vaya! ha ocurrido un error al agregar el jugador', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:jugadores')

    else:
        if equipo_id != 0:
            equipo   = get_object_or_404(Equipo, id=equipo_id)
            context['equipo'] = equipo
            form = JugadorForm(initial={'equipo': equipo, 'liga': equipo.liga})
        else:
            form = JugadorForm()

        context['form'] = form
    
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/jugadores/create_jugador.html', context)

def detail_jugador(request, jugador_id):
    context = {}
    context['zona'] = 'jugadores'
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    context['jugador'] = jugador

    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/jugadores/detail_jugador.html', context)

def edit_jugador(request, jugador_id):
    context = {}
    context['zona'] = 'jugadores'
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    if request.method == 'POST':
        try:
            form = JugadorForm(request.POST, request.FILES, instance=jugador)
            if form.is_valid():
                form.save()
                mensaje = {'desc':'El jugador se ha actualizado correctamente', 'tipo':'success'}
            else:
                print(form.errors)
                mensaje = {'desc':'Vaya! ha ocurrido un error al validar', 'tipo':'danger'}

            request.session['mensaje'] = mensaje
            return redirect('miliga:detail_jugador', jugador_id=jugador.id)

        except Exception as e:
            print('EXCEPTION______')
            print(e)
            mensaje = {'desc':'Vaya! ha ocurrido un error al actualizar el jugador', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:detail_jugador', jugador_id=jugador.id)
    else:
        form = JugadorForm(instance=jugador)
    
    context['form'] = form
    context['jugador'] = jugador
    return render(request, 'miliga/jugadores/edit_jugador.html', context)

def delete_jugador(request, jugador_id):
    context = {}
    try:
        jugador = get_object_or_404(Jugador, pk=jugador_id)
        jugador.delete()
        mensaje = {'desc':'El jugador %s se ha eliminado correctamente'%jugador.nombre, 'tipo':'success'}
    except:
        mensaje = {'desc':'Error al intentar eliminar jugador', 'tipo':'danger'}

    request.session['mensaje'] = mensaje
    return redirect('miliga:detail_equipo',jugador.equipo.id)


def create_jugadores_archivo(request,equipo_id=0):
    print('CREATE JUGADOR ARCHIVO')
    iguales={
        "Nombre"                        : "nombre"           ,
        "Teléfono"                      : "telefono"         ,
        "Numero Playera"                : "numero_playera"   ,
        "Fecha de nacimiento (dd-mm-aa)": "fecha_nacimiento" ,
    }
    ls_ingresos = []
    if request.method == 'POST':
        archivo_excel = request.FILES['archivo_jugadores']
        extension = archivo_excel.name.split('.')[-1]
        print('EXTENSION______')
        print(extension)
        if extension in ['xls', 'xlsx']:
            try:
                df = pd.read_excel(archivo_excel)
                df = df.fillna('Vacio_99')
                for index, row in df.iterrows():
                    dic_ingresos = {}
                    for col, val in row.items():
                        if val == 'Vacio_99':
                            val = None
                        dic_ingresos[iguales[col]]=val
                    ls_ingresos.append(dic_ingresos)

                equipo = get_object_or_404(Equipo, id=equipo_id)
                for i in ls_ingresos:
                    if i['fecha_nacimiento']:
                        fecha_str = i['fecha_nacimiento']
                        fecha_obj = datetime.strptime(fecha_str, "%d-%m-%Y")
                        fecha_formateada = fecha_obj.strftime("%Y-%m-%d")
                        i['fecha_nacimiento'] = fecha_formateada

                    jugador = Jugador(
                        equipo = equipo,
                        liga = equipo.liga,
                        nombre = i['nombre'],
                        telefono = i['telefono'],
                        ocupacion = i['ocupacion'],
                        jugador_img = i['jugador_img'],
                        numero_playera = i['numero_playera'],
                        fecha_nacimiento = i['fecha_nacimiento'],
                    )
                    jugador.save()
                    mensaje = {'desc':'Jugadores agregados', 'tipo':'success'}
            except Exception as e:
                print('EXCEPTION______')
                print(e)
                mensaje = {'desc':'Error al ingresar datos', 'tipo':'danger'}
            
        else:
            mensaje = {'desc':'Error con el archivo', 'tipo':'danger'}
        request.session['mensaje'] = mensaje
    return redirect('miliga:detail_equipo',equipo_id)


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
from django.shortcuts import render
from datetime import datetime
from miliga.models import *
from miliga.forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
import pandas as pd
from django.db.models import Count
from django.contrib.auth.decorators import login_required

def jugadores(request):
    context = {}
    context['zona'] = 'jugadores'

    jugadores = Jugador.objects.all().order_by('-equipo')
    equipos = Equipo.objects.prefetch_related('jugador_set').annotate(num_jugadores=Count('jugador')).order_by('-num_jugadores')
    context['jugadores'] = jugadores
    context['equipos'] = equipos
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/jugadores/jugadores.html', context)

@login_required
def create_jugador(request,equipo_id=0):
    context = {}
    context['zona'] = 'jugadores'

    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = {'desc':'El Jugador se ha agregado correctamente', 'tipo':'success'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:detail_equipo', equipo_id=equipo_id)
        else:
            mensaje = {'desc':'Vaya! ha ocurrido un error al agregar el jugador', 'tipo':'danger'}
            request.session['mensaje'] = mensaje
            return redirect('miliga:jugadores')

    else:
        if equipo_id != 0:
            equipo   = get_object_or_404(Equipo, id=equipo_id)
            context['equipo'] = equipo
            form = JugadorForm(initial={'equipo': equipo})
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

@login_required
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

@login_required
def subir_img_jugador(request,jugador_id):
    context = {}
    context['zona'] = 'jugadores'
    if request.method == 'POST':
        jugador = get_object_or_404(Jugador, pk=jugador_id)
        try:
            jugador.jugador_img = request.FILES['jugador_img']
            jugador.save()
            mensaje = {'desc':'La imagen se ha subido correctamente', 'tipo':'success'}
        except:
            mensaje = {'desc':'Error al subir imagen', 'tipo':'danger'}

        request.session['mensaje'] = mensaje
        return redirect('miliga:detail_jugador', jugador_id=jugador.id)

    return redirect('miliga:jugadores')


@login_required
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

@login_required
def create_jugadores_archivo(request,equipo_id=0):
    print('CREATE JUGADOR ARCHIVO')
    iguales={
        "Nombre (*obligatorio)"         : "nombre"           ,
        "Teléfono"                      : "telefono"         ,
        "Numero Playera"                : "numero_playera"   ,
        "Fecha de nacimiento (dd-mm-aa) (*obligatorio)": "fecha_nacimiento" ,
    }
    ls_ingresos = []
    if request.method == 'POST':
        archivo_excel = request.FILES['archivo_jugadores']
        extension = archivo_excel.name.split('.')[-1]
        if extension in ['xls', 'xlsx']:
            try:
                df = pd.read_excel(archivo_excel)
                df = df.fillna('Vacio_codigo##10')
                for index, row in df.iterrows():
                    dic_ingresos = {}
                    for col, val in row.items():
                        if val == 'Vacio_codigo##10':
                            val = None
                        if iguales[col] == 'fecha_nacimiento' or iguales[col] == 'nombre':
                            if val == None:
                                mensaje = {'desc':'Error, un campo obligatorio se encuentra vacío', 'tipo':'danger'}
                                request.session['mensaje'] = mensaje
                                return redirect('miliga:detail_equipo',equipo_id)
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
                        nombre = i['nombre'],
                        telefono = i['telefono'],
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




def comprobar_mensajes(request, context):
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return context
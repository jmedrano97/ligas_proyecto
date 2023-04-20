from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

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
    
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
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
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return render(request, 'miliga/equipos/detail_equipo.html', context)

def edit_equipo(request, equipo_id):
    context = {}
    context['zona'] = 'equipos'

    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('miliga:detail_equipo', equipo_id=equipo.id)
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

    jugadores = Jugador.objects.all().order_by('-id')
    context['jugadores'] = jugadores
    return render(request, 'miliga/jugadores/jugadores.html', context)



def create_jugador(request,equipo_id=0):
    context = {}
    context['zona'] = 'jugadores'

    if request.method == 'POST':
        try:
            form = JugadorForm(request.POST, request.FILES)
            print('CRATE______')
            print(form)
            if form.is_valid():
                form.save()
                return redirect('miliga:jugadores')
        except:
            form = JugadorForm()
            context['form'] = form
            context['mensaje'] = 'Vaya! ha ocurrido un error al crear el jugador'
            return render(request, 'miliga/jugadores/create_jugador.html', context)
    else:
        print('GET______')
        if equipo_id != 0:
            equipo   = get_object_or_404(Equipo, id=equipo_id)
            context['equipo'] = equipo
            form = JugadorForm(initial={'equipo': equipo, 'liga': equipo.liga})
        else:
            form = JugadorForm()

        context['form'] = form

    return render(request, 'miliga/jugadores/create_jugador.html', context)

def detail_jugador(request, jugador_id):
    context = {}
    context['zona'] = 'jugadores'
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    context['jugador'] = jugador

    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']

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
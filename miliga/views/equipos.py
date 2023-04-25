from django.shortcuts import render
from miliga.models import *
from miliga.forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

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


def comprobar_mensajes(request, context):
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return context
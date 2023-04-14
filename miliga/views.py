from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return redirect('miliga:equipos')  

def index(request):
    return render(request, 'miliga/index.html')



def equipos(request):
    equipos = Equipo.objects.all().order_by('-id')
    return render(request, 'miliga/equipos/equipos.html', {'equipos':equipos})

def create_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('miliga:equipos')
    else:
        form = EquipoForm()
    return render(request, 'miliga/equipos/create_equipo.html', {'form':form})

def detail_equipo(request, equipo_id):
    context = {}
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo_id)
    context['equipo'] = equipo
    context['jugadores'] = jugadores
    return render(request, 'miliga/equipos/detail_equipo.html', context)

def edit_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('miliga:detail_equipo', equipo_id=equipo.id)
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'miliga/equipos/edit_equipo.html', {'form':form, 'equipo':equipo})





def jugadores(request):
    jugadores = Jugador.objects.all().order_by('-id')
    return render(request, 'miliga/jugadores/jugadores.html', {'jugadores':jugadores})

def create_jugador(request,equipo_id=0):
    context = {}
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('miliga:jugadores')
    else:
        if equipo_id != 0:
            equipo   = get_object_or_404(Equipo, id=equipo_id)
            context['equipo'] = equipo
            form = JugadorForm(initial={'equipo': equipo, 'liga': equipo.liga})
        else:
            form = JugadorForm()

        context['form'] = form

    return render(request, 'miliga/jugadores/create_jugador.html', context)

def detail_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    return render(request, 'miliga/jugadores/detail_jugador.html', {'jugador':jugador})
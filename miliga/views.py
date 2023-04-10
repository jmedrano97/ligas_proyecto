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
    return render(request, 'miliga/equipos.html', {'equipos':equipos})

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
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    return render(request, 'miliga/equipos/detail_equipo.html', {'equipo':equipo})



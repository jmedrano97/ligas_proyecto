import itertools
import random
import datetime
from django.shortcuts import render
from miliga.models import *
from miliga.forms import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db import transaction
# Create your views here.

def posiciones(request):
    context = {}
    context['zona'] = 'posiciones'
    equipos = Equipo.objects.all().order_by('-puntuacion')
    context['equipos'] = equipos
    jornadas = Jornada.objects.prefetch_related('partido_set').order_by('-numero')
    context['jornadas'] = jornadas
    return render(request, 'miliga/posiciones.html',context)

def matches(request):
    context = {}
    context['zona'] = 'matches'
    jornadas = Jornada.objects.prefetch_related('partido_set').order_by('-numero')
    context['jornadas'] = jornadas
    context = comprobar_mensajes(request, context)
    return render(request, 'miliga/matches.html',context)

def finalizar_partido(request, opcion ,partido_id):
    op = False
    if opcion == 1:
        op = True
    partido = get_object_or_404(Partido, id=partido_id)
    partido.finalizado = op
    partido.save()
    return redirect('miliga:matches')

def crear_jornada(request):
    # obtener ultima jornada
    if Jornada.objects.exists():
        ultima_jornada  = Jornada.objects.all().order_by('-numero').first()
        jornada_acutual = ultima_jornada.numero+1
        jornada = Jornada(numero=jornada_acutual)
        jornada.save()
    else:
        jornada = Jornada(numero=1,vuelta=1)
        jornada.save()
    vuelta=jornada.vuelta

    # obtner campo de juego random
    campo = CampoDeJuego.objects.all().order_by('?').first()
    # obtener equipos
    equipos = list(Equipo.objects.all().order_by('?'))
    # Generamos todas las combinaciones de dos equipos sin repetir
    parejas = list(itertools.combinations(equipos, 2))
    random.shuffle(parejas)
    rolados_ls = []

    fecha = datetime.date.today()

    for i, pareja in enumerate(parejas):
        # Solo creamos un partido si el equipo local no ha jugado contra el equipo visitante en esta vuelta
        if pareja[0] not in rolados_ls and pareja[1] not in rolados_ls:
            if not Partido.objects.filter(equipo_local=pareja[0], equipo_visitante=pareja[1], jornada__vuelta=vuelta).exists():
                rolados_ls.append(pareja[0])
                rolados_ls.append(pareja[1])
                partido = Partido(fecha=fecha,campo_juego=campo,jornada=jornada,equipo_local=pareja[0], equipo_visitante=pareja[1])
                partido.save()
    
    return redirect('miliga:matches')

def confirmar_resultado(request, partido_id):
    context = {}
    if request.method == 'POST':
        partido = get_object_or_404(Partido, id=partido_id)
        goles_local= request.POST['goles_local']            if 'goles_local'    in request.POST else None
        goles_visitante= request.POST['goles_visitante']    if 'goles_visitante' in request.POST else None
        try:
            with transaction.atomic():
                goles_local = int(goles_local)
                goles_visitante = int(goles_visitante)

                partido.goles_local = goles_local
                partido.goles_visitante = goles_visitante
                partido.hora_terminacion = datetime.datetime.now() 
                partido.finalizado = True
                partido.resultado_confirmado = True
                partido.save()

                if goles_local > goles_visitante:
                    partido.equipo_local.agregar_partido_ganado(goles_a_favor=goles_local, goles_en_contra=goles_visitante)
                    partido.equipo_visitante.agregar_partido_perdido(goles_a_favor=goles_visitante, goles_en_contra=goles_local)
                elif goles_local == goles_visitante:
                    partido.equipo_local.agregar_partido_empatado(goles_a_favor=goles_local, goles_en_contra=goles_visitante)
                    partido.equipo_visitante.agregar_partido_empatado(goles_a_favor=goles_local, goles_en_contra=goles_visitante)
                elif goles_local < goles_visitante:
                    partido.equipo_local.agregar_partido_perdido(goles_a_favor=goles_local, goles_en_contra=goles_visitante)
                    partido.equipo_visitante.agregar_partido_ganado(goles_a_favor=goles_visitante, goles_en_contra=goles_local)

                # Obtener la última jornada
                jornada_actual = get_object_or_404(Jornada, id=partido.jornada.id)

                # Buscar si hay algún partido sin confirmar
                partidos_sin_confirmar = Partido.objects.filter(jornada=jornada_actual, resultado_confirmado=False)

                # Si no hay partidos sin confirmar, marcar la jornada como terminada
                if not partidos_sin_confirmar:
                    jornada_actual.jornada_terminada = True
                    jornada_actual.save()

            mensaje = {'desc':'Resultado confirmado', 'tipo':'success'}
            request.session['mensaje'] = mensaje
        except Exception as e:
            print('Error-----------')
            print(e)
            mensaje = {'desc':'Error al confirmar resultado', 'tipo':'danger'}
            request.session['mensaje'] = mensaje

    return redirect('miliga:matches')

    

def comprobar_mensajes(request, context):
    if 'mensaje' in request.session:
        context['mensaje'] = request.session.get('mensaje')
        del request.session['mensaje']
    return context
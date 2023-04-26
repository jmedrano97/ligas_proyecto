from django.contrib import admin
from .models import  Equipo, Jugador, CampoDeJuego, Partido, Clasificacion

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'campo', 'escudo_img')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre','ocupacion','equipo', 'jugador_img')
    list_filter = ('ocupacion', 'equipo')

@admin.register(CampoDeJuego)
class CampoDeJuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_inicio', 'hora_terminacion', 'campo_juego', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante')
    list_filter = ('fecha', 'campo_juego')

@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'puntuacion', 'posicion', 'goles_a_favor', 'goles_en_contra', 'diferencia_goles')

from django.contrib import admin
from .models import Liga, Equipo, Jugador, CampoDeJuego, Partido, Clasificacion

@admin.register(Liga)
class LigaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'estado', 'pais', 'fecha_inicio', 'fecha_final')

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'campo', 'liga')

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento', 'ocupacion', 'numero', 'equipo', 'liga')
    list_filter = ('ocupacion', 'equipo', 'liga')

@admin.register(CampoDeJuego)
class CampoDeJuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'liga')

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_inicio', 'hora_terminacion', 'campo_juego', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante', 'liga')
    list_filter = ('fecha', 'campo_juego', 'liga')

@admin.register(Clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'puntuacion', 'posicion', 'goles_a_favor', 'goles_en_contra', 'diferencia_goles', 'liga')
    list_filter = ('liga',)

from django.urls import path
from django.contrib import admin
from . import views


app_name = 'miliga'

urlpatterns = [
    
    path('home', views.home, name='home'),
    path('', views.index, name='index'),

    path('equipos', views.equipos, name='equipos'),
    path('create_equipo', views.create_equipo, name='create_equipo'),
    path('equipo/<int:equipo_id>/',  views.detail_equipo, name='detail_equipo'),
    path('equipo/editar/<int:equipo_id>/',  views.edit_equipo, name='edit_equipo'),
    path('equipo/eliminar/<int:equipo_id>/',  views.delete_equipo, name='delete_equipo'),

    path('jugadores', views.jugadores, name='jugadores'),
    path('create_jugador/<int:equipo_id>/', views.create_jugador, name='create_jugador'),
    path('jugador/<int:jugador_id>/',  views.detail_jugador, name='detail_jugador'),
    path('jugador/editar/<int:jugador_id>/',  views.edit_jugador, name='edit_jugador'),
    path('jugador/eliminar/<int:jugador_id>/',  views.delete_jugador, name='delete_jugador'),

]

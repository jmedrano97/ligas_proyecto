from django.urls import path
from miliga.views.equipos import equipos,create_equipo,detail_equipo,edit_equipo,delete_equipo
from miliga.views.general import index,matches,download_template,download_ejemplo
from miliga.views.jugadores import jugadores,create_jugador,detail_jugador,edit_jugador,delete_jugador,create_jugadores_archivo


app_name = 'miliga'

urlpatterns = [
    
    path('', index, name='index'),
    path('matches', matches, name='matches'),

    path('equipos', equipos, name='equipos'),
    path('create_equipo', create_equipo, name='create_equipo'),
    path('equipo/<int:equipo_id>/',  detail_equipo, name='detail_equipo'),
    path('equipo/editar/<int:equipo_id>/',  edit_equipo, name='edit_equipo'),
    path('equipo/eliminar/<int:equipo_id>/',  delete_equipo, name='delete_equipo'),

    path('jugadores', jugadores, name='jugadores'),
    path('create_jugador/<int:equipo_id>/', create_jugador, name='create_jugador'),
    path('jugador/<int:jugador_id>/',  detail_jugador, name='detail_jugador'),
    path('jugador/editar/<int:jugador_id>/',  edit_jugador, name='edit_jugador'),
    path('jugador/eliminar/<int:jugador_id>/',  delete_jugador, name='delete_jugador'),
    path('create_jugadores_archivo/<int:equipo_id>/', create_jugadores_archivo, name='create_jugadores_archivo'),

    path('download/<int:equipo_id>/', download_template, name='download_template'),
    path('download_ejemplo/<int:equipo_id>/', download_ejemplo, name='download_ejemplo'),

]

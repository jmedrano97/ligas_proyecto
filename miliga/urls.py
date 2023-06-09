from django.urls import path
from miliga.views.equipos import equipos,create_equipo,detail_equipo,edit_equipo,delete_equipo
from miliga.views.general import index,download_template,download_ejemplo,registrarse,salir,iniciar_sesion,contacto, download_cv
from miliga.views.jugadores import jugadores,create_jugador,detail_jugador,edit_jugador,delete_jugador,create_jugadores_archivo,subir_img_jugador
from miliga.views.matches import posiciones,matches,finalizar_partido,crear_jornada,confirmar_resultado
# login_required
from django.contrib.auth.decorators import login_required


app_name = 'miliga'

urlpatterns = [
    
    path('', index, name='index'),
    path('registrarse', registrarse, name='registrarse'),
    path('salir', salir, name='salir'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('contacto', contacto, name='contacto'),
    path('download_cv', download_cv, name='download_cv'),

    path('matches', matches, name='matches'),
    path('posiciones', posiciones, name='posiciones'),
    path('finalizar_partido/<int:opcion>/<int:partido_id>/', finalizar_partido, name='finalizar_partido'),
    path('crear_jornada', crear_jornada, name='crear_jornada'),
    path('confirmar_resultado/<int:partido_id>/', confirmar_resultado, name='confirmar_resultado'),


    path('equipos', equipos, name='equipos'),
    path('create_equipo', create_equipo, name='create_equipo'),
    path('equipo/<int:equipo_id>/',  detail_equipo, name='detail_equipo'),
    path('equipo/editar/<int:equipo_id>/',  edit_equipo, name='edit_equipo'),
    path('equipo/eliminar/<int:equipo_id>/',  delete_equipo, name='delete_equipo'),

    path('jugadores', jugadores, name='jugadores'),
    path('create_jugador/<int:equipo_id>/', create_jugador, name='create_jugador'),
    path('jugador/<int:jugador_id>/',  detail_jugador, name='detail_jugador'),
    path('jugador/editar/<int:jugador_id>/',  edit_jugador, name='edit_jugador'),
    path('jugador/subir_img_jugador/<int:jugador_id>/',  subir_img_jugador, name='subir_img_jugador'),
    path('jugador/eliminar/<int:jugador_id>/',  delete_jugador, name='delete_jugador'),
    path('create_jugadores_archivo/<int:equipo_id>/', create_jugadores_archivo, name='create_jugadores_archivo'),

    path('download/<int:equipo_id>/', download_template, name='download_template'),
    path('download_ejemplo/<int:equipo_id>/', download_ejemplo, name='download_ejemplo'),

]

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

]

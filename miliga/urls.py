from django.urls import path
from . import views

app_name = 'miliga'

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('equipos', views.equipos, name='equipos'),

]

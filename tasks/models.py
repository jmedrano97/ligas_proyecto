from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title + ' | ' + str(self.user)
    




# from django.db import models

# class Equipo(models.Model):
#     nombre = models.CharField(max_length=50)
#     ciudad = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nombre

# class Jugador(models.Model):
#     nombre = models.CharField(max_length=50)
#     fecha_nacimiento = models.DateField()
#     equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

# class Partido(models.Model):
#     fecha = models.DateField()
#     hora = models.TimeField()
#     estadio = models.CharField(max_length=50)
#     equipo_local = models.ForeignKey(Equipo, related_name='partidos_local', on_delete=models.CASCADE)
#     equipo_visitante = models.ForeignKey(Equipo, related_name='partidos_visitante', on_delete=models.CASCADE)
#     goles_local = models.PositiveIntegerField()
#     goles_visitante = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.equipo_local} vs. {self.equipo_visitante}"

# class Clasificacion(models.Model):
#     equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
#     posicion = models.PositiveIntegerField()
#     puntos = models.PositiveIntegerField()
#     partidos_jugados = models.PositiveIntegerField()
#     partidos_ganados = models.PositiveIntegerField()
#     partidos_empatados = models.PositiveIntegerField()
#     partidos_perdidos = models.PositiveIntegerField()
#     goles_favor = models.PositiveIntegerField()
#     goles_contra = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.equipo} - Posición {self.posicion}"

# class EstadisticasJugador(models.Model):
#     jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
#     goles = models.PositiveIntegerField()
#     asistencias = models.PositiveIntegerField()
#     tarjetas_amarillas = models.PositiveIntegerField()
#     tarjetas_rojas = models.PositiveIntegerField()

#     def __str__(self):
#         return f"Estadísticas de {self.jugador}"

from django.db import models

class Liga(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField( null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Ligas"
    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    campo = models.CharField(max_length=100, blank=True, null=True, default=None)
    telefono            = models.CharField(max_length=100, blank=True, null=True, default=None)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    escudo_img = models.ImageField(upload_to='equipos/', blank=True, null=True)
    foto_img = models.ImageField(upload_to='equipos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    # escribir opciones de posicion
    ocupacion = (
        ('Jugador', 'Jugador'),
        ('Director tecnico', 'Director tecnico'),
        ('Auxiliar', 'Auxiliar'),
    )
    nombre              = models.CharField(max_length=100)
    telefono            = models.CharField(max_length=100, blank=True, null=True, default=None)
    fecha_nacimiento    = models.DateField()
    ocupacion           = models.CharField(max_length=100,null=True, blank=True, choices=ocupacion , default='Jugador')
    numero_playera      = models.IntegerField(null=True, blank=True)
    equipo              = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    liga                = models.ForeignKey(Liga, on_delete=models.CASCADE)
    jugador_img         = models.ImageField(upload_to='jugadores/', blank=True, null=True)
    identificacion_img  = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class CampoDeJuego(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_terminacion = models.TimeField()
    campo_juego = models.ForeignKey(CampoDeJuego, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    goles_local = models.PositiveIntegerField()
    goles_visitante = models.PositiveIntegerField()
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('fecha', 'hora_inicio', 'campo_juego')
    def __str__(self):
        return self.fecha
    
class Clasificacion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    posicion = models.IntegerField()
    goles_a_favor = models.IntegerField()
    goles_en_contra = models.IntegerField()
    diferencia_goles = models.IntegerField()
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.equipo

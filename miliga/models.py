from django.db import models

class Equipo(models.Model):
    nombre     = models.CharField(max_length=100)
    campo      = models.CharField(max_length=100, blank=True, null=True, default=None)
    telefono   = models.CharField(max_length=100, blank=True, null=True, default=None)
    escudo_img = models.ImageField(upload_to='equipos/', blank=True, null=True)
    foto_img   = models.ImageField(upload_to='equipos/', blank=True, null=True)
    activo     = models.BooleanField(default=True)

    partidos_juados    = models.IntegerField(default=0)
    puntuacion         = models.IntegerField(default=0)
    partidos_ganados   = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    partidos_perdidos  = models.IntegerField(default=0)
    goles_a_favor      = models.IntegerField(default=0)
    goles_en_contra    = models.IntegerField(default=0)
    diferencia_goles   = models.IntegerField(default=0)

    def agregar_partido_ganado(self, goles_a_favor, goles_en_contra):
        self.partidos_juados += 1
        self.puntuacion += 3
        self.partidos_ganados += 1
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        self.diferencia_goles = self.goles_a_favor - self.goles_en_contra
        self.save()
    
    def agregar_partido_empatado(self, goles_a_favor, goles_en_contra):
        self.partidos_juados += 1
        self.puntuacion += 1
        self.partidos_empatados += 1
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        self.diferencia_goles = self.goles_a_favor - self.goles_en_contra
        self.save()
    
    def agregar_partido_perdido(self, goles_a_favor, goles_en_contra):
        self.partidos_juados += 1
        self.partidos_perdidos += 1
        self.goles_a_favor += goles_a_favor
        self.goles_en_contra += goles_en_contra
        self.diferencia_goles = self.goles_a_favor - self.goles_en_contra
        self.save()
    
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
    jugador_img         = models.ImageField(upload_to='jugadores/', blank=True, null=True)
    identificacion_img  = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Jornada(models.Model):
    numero = models.IntegerField()
    vuelta = models.IntegerField(default=1)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_terminacion = models.DateField(blank=True, null=True)
    jornada_terminada     = models.BooleanField(default=False)

    def __str__(self):
        return str(self.numero)


class CampoDeJuego(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    fecha            = models.DateField()
    hora_inicio      = models.TimeField(blank=True, null=True)
    hora_terminacion = models.TimeField(blank=True, null=True)
    campo_juego      = models.ForeignKey(CampoDeJuego, on_delete=models.CASCADE)
    equipo_local     = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    goles_local      = models.PositiveIntegerField(blank=True, null=True)
    goles_visitante  = models.PositiveIntegerField(blank=True, null=True)
    jornada          = models.ForeignKey(Jornada, on_delete=models.CASCADE, default=0)
    finalizado       = models.BooleanField(default=False)
    resultado_confirmado       = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('fecha', 'hora_inicio', 'campo_juego')
    def __str__(self):
        return self.equipo_local.nombre + ' vs ' + self.equipo_visitante.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100,blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefono = models.CharField(max_length=100,blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
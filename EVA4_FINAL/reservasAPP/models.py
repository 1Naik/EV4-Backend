from django.db import models

# Create your models here.
class Reserva(models.Model):

    ESTADOS = [
        ('RESERVADO','Reservado'),
        ('COMPLETADA','Completada'),
        ('ANULADA','Anulada'),
        ('NO ASISTEN','No asisten'),
    ]

    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=30)
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveSmallIntegerField()
    estado = models.CharField(max_length=15, choices=ESTADOS, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Reserva de {self.nombre} - {self.fecha_reserva} {self.hora}'

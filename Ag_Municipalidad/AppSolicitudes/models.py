from django.db import models
from django.utils import timezone
from datetime import timedelta

ESTADO_SOLICITUD = [
    ('pendiente', 'Pendiente'),
    ('aceptada', 'Aceptada'),
    ('rechazada', 'Rechazada'),
    ('expirada', 'Expirada'),
]

class Solicitud(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    comuna = models.CharField(max_length=50)
    estado = models.CharField(max_length=10, choices=ESTADO_SOLICITUD, default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_aceptacion = models.DateTimeField(null=True, blank=True)  # Campo para la fecha de aceptación

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.rut}"
    
    def ha_expirado(self):
        """Verifica si la solicitud ha expirado."""
        # La fecha de expiración es 30 días después de la fecha de solicitud
        return timezone.now() > self.fecha_solicitud + timedelta(days=30)



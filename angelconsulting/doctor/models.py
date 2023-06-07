from django.db import models

class Cita(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 50)
    solicitud = models.TextField(blank = True)
    fecha_solicitud = models.DateField(auto_now_add = True)
    aceptado = models.BooleanField(default = False)
    fecha_aceptado = models.DateField(auto_now_add = False, null = True, blank = True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ['-sent_date']

# Create your models here.

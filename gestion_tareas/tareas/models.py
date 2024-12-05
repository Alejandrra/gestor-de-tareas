from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100, null=True, blank=True)
    titulo = models.CharField(max_length=200, default="Nueva Tarea")  # Default value added
    fecha_vencimiento = models.DateField(null=True, blank=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

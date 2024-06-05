from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    archivo_pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creado_por')
    editado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='editado_por')

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

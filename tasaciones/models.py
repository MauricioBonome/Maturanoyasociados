from django.db import models

class Tasacion(models.Model):
    nombre_titular = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    direccion = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    impuesto_inmobiliario = models.FileField(upload_to='impuestos/')
    email = models.EmailField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_titular

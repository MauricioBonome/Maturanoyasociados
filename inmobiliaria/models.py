from django.db import models




class Property(models.Model):
    PROPERTY_TYPES = (
        ('Venta', 'Venta'),
        ('Alquiler', 'Alquiler'),
        ('Alquiler Temporario', 'Alquiler Temporario'),
        ('Tasaciones', 'Tasaciones'),
    )
    title = models.CharField(max_length=255)

    description = models.TextField()
    location = models.CharField(max_length=255, default='Sin ubicación')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendido = models.BooleanField(default=False)
    alquilado= models.BooleanField(default=False)




    def __str__(self):
        return self.title

    def get_image_by_index(self, index):
        try:
            return self.images.all()[index]
        except IndexError:
            return None


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return f'{self.property.title} - Imagen {self.id}'


class Venta(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    comentarios = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
from django.db import models

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')

class Contacto(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    inquiry_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
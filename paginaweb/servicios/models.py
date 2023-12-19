from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo

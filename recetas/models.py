from django.db import models

# Create your models here.
class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre_receta
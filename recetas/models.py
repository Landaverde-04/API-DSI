from django.db import models

# Create your models here.
class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()
    tipo = models.CharField(max_length=100, null=True, blank=True)
    extras = models.CharField(max_length=100, null=True, blank=True)

    
    def __str__(self):
        return self.nombre_receta
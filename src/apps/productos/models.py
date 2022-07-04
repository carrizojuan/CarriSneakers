from pyexpat import model
from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to = "productos", null=True)

    class Meta:
        db_table = "productos"

    def __str__(self):
        return self.nombre
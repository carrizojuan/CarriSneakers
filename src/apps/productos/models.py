from pyexpat import model
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=250)

    class Meta:
        db_table = "marcas"
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to = "productos", null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="productos_relacionados", null=True)

    class Meta:
        db_table = "productos"

    def __str__(self):
        return self.nombre


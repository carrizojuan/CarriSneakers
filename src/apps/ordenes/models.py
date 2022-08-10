from msilib.schema import Property
from django.db import models
from apps.productos.models import Producto
from apps.usuarios.models import Usuario

# Create your models here.

class Orden(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    @property
    def get_total_carrito(self):
        ordenitems = self.ordenitem_set.all()
        total = sum([item.get_total for item in ordenitems])
        return total

    @property
    def get_cant_items(self):
        ordenitems = self.ordenitem_set.all()
        cantidad = sum([item.cantidad for item in ordenitems])
        return cantidad

    def __str__(self):
        return str(self.id)

class OrdenItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(null=True, default=0, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.cantidad * self.producto.precio
        return total

    def __str__(self):
        return str(self.producto.nombre)

class DirecconEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=255, null=False)
    ciudad = models.CharField(max_length=255, null=False)
    provincia = models.CharField(max_length=255, null=False)
    codigo_postal = models.CharField(max_length=255, null=False)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.direccion)


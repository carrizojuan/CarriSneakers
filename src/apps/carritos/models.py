from django.db import models

from apps.productos.models import Producto
from apps.usuarios.models  import Usuario

class Carrito(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return self.usuario.username

class Item(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
	cantidad = models.IntegerField()

from pyexpat import model
from django.db import models

from apps.productos.models import Producto
from apps.usuarios.models  import Usuario

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, related_name = "comentarios",on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.producto.nombre} | {self.usuario}")
    
    class Meta:
        db_table = "comentarios"
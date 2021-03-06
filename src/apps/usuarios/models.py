from distutils.command import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    foto = models.ImageField(upload_to = "perfil", null=True)
    #favoritos = models.ManyToManyField(Producto)

    class Meta:
        db_table = "usuarios"
    
    
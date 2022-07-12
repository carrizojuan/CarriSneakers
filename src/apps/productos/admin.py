from django.contrib import admin
from .models import Producto, Marca
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","nombre", "precio", "cantidad", "activo", "marca"]

admin.site.register(Producto, ProductoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ["id","nombre"]

admin.site.register(Marca, MarcaAdmin)

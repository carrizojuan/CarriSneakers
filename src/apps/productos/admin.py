from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "cantidad", "activo"]

admin.site.register(Producto, ProductoAdmin)
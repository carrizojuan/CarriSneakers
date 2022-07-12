from django.contrib import admin

from .models import Carrito, Item

class CarritoAdmin(admin.ModelAdmin):
	list_display = ["id","usuario"]

admin.site.register(Carrito, CarritoAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ["id","carrito", "producto", "cantidad"]

admin.site.register(Item, ItemAdmin)

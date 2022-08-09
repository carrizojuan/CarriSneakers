from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Orden)
admin.site.register(models.OrdenItem)
admin.site.register(models.DirecconEnvio)

from re import template
from django.shortcuts import render
from apps.productos.models import Producto

def inicio(request):
    template_name = "index.html"
    ctx = {
        "ult_productos": Producto.objects.all().order_by('-id')[:2]
    }
    return render(request, template_name, ctx)

def iniciarSesion(request):
    template_name = "login.html"
    return render(request, template_name, {})
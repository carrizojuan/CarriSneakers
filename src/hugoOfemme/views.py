from re import template
from django.shortcuts import render
from apps.productos.models import Productos

def inicio(request):
    template_name = "index.html"
    ctx = {
        "ult_productos": Productos.objects.all().order_by('-id')[:2]
    }
    return render(request, template_name, ctx)

def iniciarSesion(request):
    template_name = "login.html"
    return render(request, template_name, {})
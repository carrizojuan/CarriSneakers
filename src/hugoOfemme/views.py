from django.shortcuts import render
from apps.productos.models import Productos

def inicio(request):
    template_name = "index.html"
    ctx = {
        "ult_productos": Productos.objects.all()
    }
    return render(request, template_name, ctx)

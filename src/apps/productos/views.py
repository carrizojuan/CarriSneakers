from django.shortcuts import render
from .models import Productos
# Create your views here.



def listar(request):
    template_name = "productos/listar.html"
    ctx = {
        "lista_productos": Productos.objects.all()
    }
    return render(request, template_name, ctx)


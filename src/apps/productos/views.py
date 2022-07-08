from django.shortcuts import render
from .models import Producto
from django.views.generic.list import ListView
# Create your views here.


"""
def listar(request):
    template_name = "productos/listar.html"
    ctx = {
        "lista_productos": Producto.objects.all()
    }
    return render(request, template_name, ctx)
"""

class Listar(ListView):
    template_name = "productos/listar.html"
    model = Producto
    context_object_name = "lista_productos"

    def get_queryset(self):
        return Producto.objects.filter(activo=True)
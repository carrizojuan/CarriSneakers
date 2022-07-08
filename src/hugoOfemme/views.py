from re import template
from string import Template
from django.shortcuts import render
from apps.productos.models import Producto
from django.views.generic.base import TemplateView

#Vista basada en funcion
def inicio(request):
    template_name = "index.html"
    ctx = {
        "ult_productos": Producto.objects.all().order_by('-id')[:2]
    }
    return render(request, template_name, ctx)

#Vista basada en clase
class Inicio(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["ult_productos"] = Producto.objects.all().order_by('-id')[:2]
        return context
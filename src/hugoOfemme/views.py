from django.shortcuts import render
from apps.ordenes.models import Orden
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
    
def checkout(request):
    template_name = "checkout/main.html"
    if request.user.is_authenticated:
        usuario = request.user.id
        orden, creado = Orden.objects.get_or_create(
            usuario=usuario,
            completado = False
        )
        items = orden.ordenitem_set.all()
    else:
        items = []
        orden = {
            'get_total_carrito':0,
            'get_cant_items': 0
        }
    ctx = {
        'items': items,
        'orden': orden,
    }
    return render(request, template_name, ctx)

def carrito(request):
    if request.user.is_authenticated:
        usuario = request.user.id
        orden, creado = Orden.objects.get_or_create(
            usuario=usuario,
            completado = False
        )
        items = orden.ordenitem_set.all()
    else:
        items = []
        orden = {
            'get_total_carrito':0,
            'get_cant_items': 0
        }

    template_name = "carrito/main.html"
    ctx = {
        'items': items,
        'orden': orden,
    }
    return render(request, template_name, ctx)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.ordenes.models import Orden
from apps.ordenes.forms import DireccionEnvioForm
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

@login_required
def checkout(request):
    template_name = "checkout/main.html"
    form = DireccionEnvioForm()
    usuario = request.user

    orden, creado = Orden.objects.get_or_create(
        usuario=usuario,
        completado = False
    )
    items = orden.ordenitem_set.all()
    print(request.method)
    if request.method == "POST":
        print("ESTOY ADENTO DE REQUEST POST")
        form = DireccionEnvioForm(request.POST)
        if form.is_valid():
            form.instance.usuario = request.user
            form.instance.orden = orden
            form.save()
            orden.completado = True     
            orden.save()

            return redirect("inicio")

    ctx = {
        'items': items,
        'orden': orden,
        'direccion_form': form
    }
    return render(request, template_name, ctx)

@login_required
def carrito(request):
    
    usuario = request.user
    orden, creado = Orden.objects.get_or_create(
        usuario=usuario,
        completado = False
    )
    items = orden.ordenitem_set.all()

    template_name = "carrito/main.html"
    ctx = {
        'items': items,
        'orden': orden,
    }
    return render(request, template_name, ctx)
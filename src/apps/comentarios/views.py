from ast import arg
from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Comentario
from apps.productos.models import Producto
from .forms import ComentarioForm
# Create your views here.

class Agregar(CreateView):
    model = Comentario
    template_name = "productos/agregar_comentario.html"
    form_class = ComentarioForm
    success_url = reverse_lazy("productos:admin_listar")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.producto_id = self.kwargs['pk']

def agregar(request, id):
    producto = Producto.objects.get(id=id)
    form = ComentarioForm(instance=producto)
    comentarios = Comentario.objects.all().filter(producto=producto.id).order_by('comentario_id')
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=producto)
        if form.is_valid():
            usuario = request.user
            comentario = form.cleaned_data["comentario"]
            c = Comentario(producto = producto, usuario=usuario, comentario = comentario)
            c.save()
            print("Entro aca")
            return redirect("productos:detalle", id)
    else:
        form = ComentarioForm()

    context = {
        'form': form,
        'comentarios': comentarios
    }
    return render(request, 'productos/agregar_comentario.html', context)
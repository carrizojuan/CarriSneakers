from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.core.decorators import superuser_required
from apps.core.mixins import SuperUserRequiredMixin

from .models import Producto
from .forms import ProductoForm


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

# --------------------------------------------------------
#               VISTAS PARA EL ADMIN
# --------------------------------------------------------


class ListarAdmin(SuperUserRequiredMixin,LoginRequiredMixin, ListView):
    template_name = "productos/admin/listar.html"
    model = Producto
    context_object_name = "lista_productos"

    
    

class Crear(SuperUserRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "productos/admin/nuevo.html"
    model = Producto
    form_class = ProductoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_listar")

class Editar(SuperUserRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = "productos/admin/editar.html"
    model = Producto
    form_class = ProductoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("productos:admin_listar")

class Detalle(SuperUserRequiredMixin, LoginRequiredMixin, DetailView):
    model = Producto
    template_name = "productos/admin/detalle.html"


@superuser_required()
def borrar(request, pk):
    p = Producto.objects.get(id=pk)
    p.delete()
    return redirect("productos:admin_listar")
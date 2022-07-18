from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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

    def get_context_data(self, **kwargs):
        context = super(Listar, self).get_context_data(**kwargs) 
        context["nombre_producto"] = self.request.GET.get("nombre_producto", "")
        productos = Producto.objects.filter(activo=True)
        
        if self.request.user.is_authenticated:
            favoritos = []
            for p in productos:
                if p.favorito.filter(id=self.request.user.id).exists():
                    favoritos.append(p)
            context["fav_productos"] = favoritos
        return context
        
    def get_queryset(self):
        query = Producto.objects.filter(activo=True)
        nombre_producto = self.request.GET.get("nombre_producto", None)
        if nombre_producto:
            query = query.filter(nombre__icontains=nombre_producto) 
        return query
    
@superuser_required()
def producto_detalle(request, pk):
    p = get_object_or_404(Producto, id=pk)
    ctx = {
        "producto": p
    }
    if request.user.is_authenticated:
        favorito = False
        if p.favorito.filter(id=request.user.id).exists():
            favorito = True
    ctx["es_favorito"] = favorito
    return render(request, "productos/detalle.html", ctx)

@superuser_required()
def agregar_favorito(request, id):
    p = get_object_or_404(Producto, id=id)
    if p.favorito.filter(id=request.user.id).exists():
        p.favorito.remove(request.user)
    else:
        p.favorito.add(request.user)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])



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
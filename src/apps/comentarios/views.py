from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Comentario
from .forms import ComentarioForm
# Create your views here.

class Agregar(CreateView):
    model = Comentario
    template_name = "productos/agregar_comentario.html"
    form_class = ComentarioForm
    success_url = reverse_lazy("productos:admin_listar")
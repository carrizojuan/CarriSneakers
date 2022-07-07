from re import template
from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.

def registrar_usuario(request):
    template_name = "usuarios/registrar.html"
    ctx = {
        "form": UsuarioForm()
    }
    return render(request, template_name, ctx)
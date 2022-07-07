from re import template
from django.shortcuts import render
from .forms import UsuarioForm

# Create your views here.

def registrar_usuario(request):
    template_name = "usuarios/registrar.html"
    formulario = UsuarioForm()
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
        else:
            pass
    ctx = {
        "form": formulario
    }
    return render(request, template_name, ctx)
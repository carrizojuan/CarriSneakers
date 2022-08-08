from django.shortcuts import render

# Create your views here.

def visualizar(request):
    template_name = "carrito/main.html"
    return render(request, template_name)
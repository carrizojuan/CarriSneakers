from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect 
import json
from apps.ordenes.models import Orden, OrdenItem, Producto
# Create your views here.

def updateItem(request):
    data = json.loads(request.body)
    producto_id = data['producto_id']
    action = data['action']
    usuario = request.user
    producto = Producto.objects.get(id=producto_id)

    orden, creado = Orden.objects.get_or_create(
            usuario=usuario,
            completado = False
    )
    
    ordenItem, creado = OrdenItem.objects.get_or_create(
        orden=orden,
        producto = producto
    )

    if action == "add":
        ordenItem.cantidad = (ordenItem.cantidad) + 1
        print(ordenItem.cantidad)
    elif action == "remove":
        ordenItem.cantidad = (ordenItem.cantidad) - 1

    ordenItem.save()

    if ordenItem.cantidad == 0:
        ordenItem.delete()
    return JsonResponse("El producto fue agregado", safe=False)


def addItem(request, pk):
    usuario = request.user
    producto = Producto.objects.get(id=pk)
    orden, creado = Orden.objects.get_or_create(
        usuario=usuario,
        completado = False
    )
    ordenItem,creado = OrdenItem.objects.get_or_create(
        orden=orden,
        producto=producto
    )
    ordenItem.cantidad = ordenItem.cantidad + 1 
    ordenItem.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

def removeItem(request, pk):
    usuario = request.user
    producto = Producto.objects.get(id=pk)
    orden = Orden.objects.get(
        usuario=usuario,
        completado = False
    )
    ordenItem = OrdenItem.objects.get(
        orden=orden,
        producto=producto
    )
    ordenItem.cantidad = ordenItem.cantidad - 1
    ordenItem.save()
    if ordenItem.cantidad == 0:
        ordenItem.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

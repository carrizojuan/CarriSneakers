from django.urls import path
from . import views

app_name = "orden"


urlpatterns = [
    #path("ListarProductos/", views.listar, name="listar"),
    path("update_item/", views.updateItem, name="update_item")
]


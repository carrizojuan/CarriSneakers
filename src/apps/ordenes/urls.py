from django.urls import path
from . import views

app_name = "orden"


urlpatterns = [
    #path("ListarProductos/", views.listar, name="listar"),
    path("update_item/", views.updateItem, name="update_item"),
    path("add_item/<int:pk>", views.addItem, name="add_item"),
    path("remove_item/<int:pk>", views.removeItem, name="remove_item"),
]


from django.urls import path
from . import views

app_name = "productos"

urladmin = [
    path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("Admin/Nuevo/", views.Crear.as_view(), name="admin_nuevo"),
    path("Admin/Editar/<int:pk>/", views.Editar.as_view(), name="admin_editar")

]

urlsite = [
    #path("ListarProductos/", views.listar, name="listar"),
    path("Listar/", views.Listar.as_view(), name="listar")
]

urlpatterns = urladmin + urlsite

from django.urls import path
from . import views
from apps.comentarios import views as views_c

app_name = "productos"

urladmin = [
    path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("Admin/Nuevo/", views.Crear.as_view(), name="admin_nuevo"),
    path("Admin/Editar/<int:pk>/", views.Editar.as_view(), name="admin_editar"),
    path("Admin/Borrar/<int:pk>/", views.borrar, name="admin_borrar"),
    path("Admin/Detalle/<int:pk>/", views.Detalle.as_view(), name="admin_detalle"),

]

urlsite = [
    #path("ListarProductos/", views.listar, name="listar"),
    path("Listar/", views.Listar.as_view(), name="listar"),
    path("Favoritos", views.ListarFavoritos.as_view(), name="listar_favoritos"),
    path("<int:pk>/", views.producto_detalle, name="detalle"),
    path("AgregarFavorito/<int:id>/", views.manejar_favorito, name="manejar_favorito"),
    path("<int:id>/comentar", views_c.agregar, name="agregar_comentario")
]

urlpatterns = urladmin + urlsite

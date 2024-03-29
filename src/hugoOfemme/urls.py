"""hugoOfemme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Includes
    path("Productos/", include("apps.productos.urls")),
    path("Usuario/", include("apps.usuarios.urls")),
    path("", include("apps.ordenes.urls")),

    #Urls propias del proyecto
    #path("", views.inicio, name="inicio"),
    path("", views.Inicio.as_view(), name = "inicio"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("checkout/", views.checkout, name="checkout"),
    path("Carrito/", views.carrito, name="carrito"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



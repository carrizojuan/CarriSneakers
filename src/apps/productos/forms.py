from pyexpat import model
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    imagen = forms.ImageField(label="Imagen", required=False)
    class Meta:
        model = Producto
        fields = ["nombre", "activo", "precio", "cantidad", "imagen"]
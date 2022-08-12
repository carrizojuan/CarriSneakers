from pyexpat import model
from django import forms
from .models import DirecconEnvio 

class DireccionEnvioForm(forms.ModelForm):
    direccion = forms.CharField(label="Direccion", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    ciudad = forms.CharField(label="Ciudad", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    provincia = forms.CharField(label="Provincia", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    codigo_postal = forms.CharField(label="Codigo Postal", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = DirecconEnvio
        fields = ['direccion', 'ciudad', 'provincia', 'codigo_postal']
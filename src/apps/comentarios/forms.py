from logging import PlaceHolder
from pyexpat import model
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(placeholder="Agregar comentario...", required=True, widget=forms.TextInput(attrs={
        "class": "form-control"
        }))
    
    class Meta:
        model = Comentario
        fields = ["comentario"]
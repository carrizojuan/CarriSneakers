from pyexpat import model
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={
        "class": "md-textarea form-control",
        "rows": "4",
        "placeholder": "Agregar comentario"
        }))
    class Meta:
        model = Comentario
        fields = ["comentario"]
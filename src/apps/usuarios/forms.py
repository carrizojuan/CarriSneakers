from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    username = forms.CharField(label="Usuario", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirmar contraseña", required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = Usuario
        fields = ("first_name", "last_name", "username", "email")
    
    # Ejemplo de validacion de campo
    """
    def clean_username(self):
        username = self.cleaned_data["username"]
        if not username.isalpha():
            raise ValidationError("El nombre de usuario no puede contener numeros")

        return username
    """
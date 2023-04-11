from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))


class ClienteFormulario (forms.Form):
    # nombre = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Nombre",
    #             "class": "form-control"
    #         }
    #     ))
    # apellido = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Apellido",
    #             "class": "form-control"
    #         }
    #     ))
    # nacimiento = forms.DateField(
    #     widget=forms.DateInput(
    #         attrs={
    #             "placeholder": "Fecha de Nacimiento",
    #             "class": "form-control"
    #         }
    #     ))
    # direccion = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Dirección",
    #             "class": "form-control"
    #         }
    #     ))
    # usuario = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Usuario",
    #             "class": "form-control"
    #         }
    #     ))
    # clave = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Contraseña",
    #             "class": "form-control"
    #         }
    #     ))

    # class Meta:
    #     model = User
    #     fields = ('nombre', 'apellido', 'nacimiento', 'direccion', 'usuario', 'clave')

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nacimiento = forms.DateField()
    direccion = forms.CharField(max_length=40)
    usuario = forms.CharField(max_length=40)
    clave = forms.CharField(max_length=40)

class BuscarProducto(forms.Form):
    item = forms.CharField(
        label = "Buscar Item",
        widget=forms.TextInput(),
        required=False
    )
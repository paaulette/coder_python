from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .forms import LoginForm, ClienteFormulario, BuscarProducto
from django.contrib.auth import authenticate, login
import sqlite3
from apps.models import Cliente, Producto

# Create your views here.
def inicio (request):
    return render(request, "index.html")

def cliente (request):
    
    if request.method == "POST":
        form = ClienteFormulario(request.POST)

        if form.is_valid():
            datos_correctos = form.cleaned_data

            print("entra porque es valido ")
            nombre = datos_correctos['nombre']
            apellido = datos_correctos['apellido']
            nacimiento = datos_correctos['nacimiento']
            direccion = datos_correctos['direccion']
            usuario = datos_correctos['usuario']
            clave = datos_correctos['clave']
            
            cliente = Cliente(nombre = nombre, 
                              apellido = apellido, 
                              nacimiento = nacimiento, 
                              direccion = direccion, 
                              usuario = usuario, 
                              clave = clave)
            cliente.save()
        
            msg = 'Se ha registrado el usuario satisfactoriamente!'
    else:
        form = ClienteFormulario()
        msg = ''
        
    clientes =  Cliente.objects.all()

        
    context = {'form': form, 'clientes': clientes, 'message': msg}

    return render(request, "cliente.html", context)

def productos (request):
    item_a_buscar = request.GET.get('item', None)
    if item_a_buscar:
        products =  Producto.objects.filter(item__icontains = item_a_buscar)
    else:
        products =  Producto.objects.all()

    
    formulario = BuscarProducto()      
    products_dict = {'productos': products, 'formulario': formulario}

    return render(request, "productos.html", products_dict)

def register(self):
    plantilla = loader.get_template('register.html')

    documento = plantilla.render()

    return HttpResponse(documento)

def login (self):
    plantilla = loader.get_template('login.html')

    documento = plantilla.render()

    return HttpResponse(documento)


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = request.POST['usuario']
            password = request.POST['clave']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'El usuario o la contraseña son incorrectos o no existen'
        else:
            msg = 'Error validando el formulario'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})
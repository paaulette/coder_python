from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField()
    direccion = models.CharField(max_length=40)
    usuario = models.CharField(max_length=40)
    clave = models.CharField(max_length=40)


class Producto (models.Model):
    item = models.CharField(max_length=40)
    precio = models.FloatField()
    local = models.CharField(max_length=40)
    stock = models.IntegerField()

class Compras (models.Model):
    idcliente = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()
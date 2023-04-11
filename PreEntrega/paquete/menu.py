from paquete.cliente import Cliente
from paquete.producto import Producto
import json

class Menu: 
    def __init__ (self, base_de_datos):
        self.clientes = []
        self.productos = []
        self.base_de_datos = base_de_datos

    def mostrar_menu (self):
        print("1. Agregar cliente")
        print("2. Hacer compra")
        print("3. Mostrar historial de compras")
        print("4. Salir")

        self.levantar_clientes()
        self.levantar_productos()

        print(self.productos)

        while True:

            opcion_seleccionada = input("indique opción seleccionada: ")

            if opcion_seleccionada == '1': 
                self.agregar_cliente()
                break
            elif opcion_seleccionada == '2':
                self.hacer_compra()
                break
            elif opcion_seleccionada == '3':
                self.historial_compras()
                break
            elif opcion_seleccionada == '4':
                self.salir()
                break
            else:
                print("seleccione una opcion correcta")
            
    def agregar_cliente (self):
        print("Complete los siguientes datos para la creación de un cliente: ")
        while True:
            Nombre = input('Ingrese su nombre: ')

            # Valido que el Nombre no esté vacío
            if Nombre == '':
                print ("\x1b[31m** ERROR: El Nombre no debe ser vacío **\x1b[0m") 
            else:
                break
             
        while True:
            Apellido = input('Ingrese su apellido: ')

            # Valido que el Apellido no esté vacío
            if Apellido == '':
                print ("\x1b[31m** ERROR: El Apellido no debe ser vacío **\x1b[0m") 
            else: 
                break   

        while True:
            dni = input('Ingrese su DNI: ')

            # Valido que el DNI no esté vacío y 8 caracteres 
            if dni == '':
                print ("\x1b[31m** ERROR: El DNI no debe ser vacío **\x1b[0m")  
            elif len(dni) != 8:
                print ("\x1b[31m** ERROR: El DNI debe tener 8 caracteres **\x1b[0m")
            else:
                break

        while True:
            Domicilio = input('Ingrese su Domicilio: ')

            # Valido que el Domicilio no esté vacío
            if Domicilio == '':
                print ("\x1b[31m** ERROR: El Domicilio no debe ser vacío **\x1b[0m")  
            else:
                break

        while True:
            usuario = input('Ingrese nombre de usuario: ')

         # Valido que el usuario no esté vacío y su cantidad de caracteres sean entre 4 y 9 
            if usuario == '':
                print ("\x1b[31m** ERROR: El usuario no debe ser vacío **\x1b[0m") 
            elif len(usuario) < 4:
                print ("\x1b[31m** ERROR: El usuario debe tener más de 3 caracteres **\x1b[0m")  
            elif len(usuario) > 10:
                print ("\x1b[31m** ERROR: El usuario debe tener menos de 10 caracteres **\x1b[0m")
            elif usuario in self.base_de_datos:
                print ("\x1b[31m** ERROR: El usuario ya existe, elija uno diferente **\x1b[0m")
            else:
                break

        while True:
            clave = input('Ingrese Contraseña: ')

        # Valido que la clave no esté vacía y su cantidad de caracteres sean mayores a 5
            if clave == '':
                print ("\x1b[31m** ERROR: La clave no debe ser vacío **\x1b[0m")
            elif len(clave) < 5:
                print ("\x1b[31m** ERROR: La clave debe tener al menos 5 caracteres **\x1b[0m")
            else:   
                break

        cliente1 = Cliente (Nombre, Apellido, dni, Domicilio, usuario, clave)
        self.clientes.append(cliente1)

        # Pregunto si quiere seguir agregando usuarios o no para que se produzca un bucle
        while True: 
            confirmacion = input('Quiere seguir agregando usuarios? (S/N)').upper()
            if confirmacion == 'S':
                self.agregar_cliente()
                break
            elif confirmacion =='N':
                print('Gracias! Saludos')
                break
        
    def hacer_compra (self):
        print("Indique el cliente: ")


        for i, indique_cliente in enumerate(self.clientes, start=1):
            print(f"{i}: {indique_cliente.usuario}")
        
        while True:
            hacer_compra = input("Indique el código de cliente: ")
            if hacer_compra == '':
                print ("\x1b[31m** ERROR: La compra no debe ser vacío **\x1b[0m")  
            elif int(hacer_compra) > len(self.clientes):
                print ("\x1b[31m** ERROR: El código es inválido **\x1b[0m")
            else:
                break
        


        print('Seleccione el o los productos a comprar: ')
        print(self.productos)
        for producto in self.productos:
            print(str(producto.codigo) + ': '+ producto.nombre_producto + ' S' + str(producto.precio))

        while True:
            compra = input('Ingrese el producto a comprar: ')

            # Valido que la compra no esté vacía 
            if compra == '':
                print ("\x1b[31m** ERROR: La compra no debe ser vacío **\x1b[0m")  
            elif int(compra) > len(self.productos):
                print ("\x1b[31m** ERROR: El código es inválido **\x1b[0m")
            else:
                break
        

    def levantar_productos (self):
        try: 
            with open ("PreEntrega/bases/productos.json","r") as f:
                bd_productos = json.load (f)
        except FileNotFoundError:       
            print("Error: No se encuentra la base de productos") 
        
        for item in bd_productos: 
            for key,value in item.items():
                producto1 = Producto (key,
                                       value["nombre_producto"], 
                                       value["precio"], 
                                       value["stock"])
                self.productos.append(producto1)

    def levantar_clientes (self):
        try: 
            with open ("PreEntrega/bases/clientes.json","r") as f:
                bd_clientes = json.load (f)
        except FileNotFoundError:       
            print("Error: No se encuentra la base de clientes") 
        
        
        for key, value in bd_clientes.items():
            cliente1 = Cliente (value["nombre"], 
                                value["apellido"], 
                                value["dni"],
                                value["domicilio"],
                                key,
                                value ["clave"],
                                value ["historial"],
                                )
            self.clientes.append(cliente1)
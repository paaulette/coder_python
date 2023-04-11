class Cliente: 
    def __init__ (self, nombre, apellido, dni, domicilio, usuario, clave, historial):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni    
        self.domicilio = domicilio
        self.usuario = usuario
        self.clave = clave
        self.historial = historial

    def __str__ (self):
       return "Nombre: "+self.nombre + "\nApellido: "+ self.apellido + "\nDNI: "+self.dni + "\nDomicilio: "+self.domicilio + "\nSexo: "+self.sexo    

    def comprar (self, item, precio, cantidad):
        posicion = len(self.historial) +1
        self.historial.update ({posicion: {"nombre_producto": item, 
                                           "precio": precio,
                                           "cantidad": cantidad}})
        print(self.nombre + " compró " + cantidad + " " + item + " a $" + precio)

    def actualizar_domicilio (self, nuevo_domicilio):  
        print("domicilio actualizado: "+self.domicilio+" por "+nuevo_domicilio)
        self.domicilio = nuevo_domicilio



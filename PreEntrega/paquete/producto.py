class Producto: 
    def __init__ (self, codigo, nombre_producto, precio, stock):
        self.codigo = codigo
        self.nombre_producto = nombre_producto
        self.precio = precio    
        self.stock = stock

    def actualizar_stock (self, nuevo_stock): 
        self.stock = nuevo_stock

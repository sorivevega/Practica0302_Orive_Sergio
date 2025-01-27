#Añadir una clase Pedido que tiene como atributos:
#    - lista de productos
#    - lista de cantidades
#Añade las siguiente funcionalidad:
#    - total_pedido: muestra el precio final del pedido
#    - mostrar_productos: muestra los productos del pedido




class Producto:


    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio


    @property
    def codigo(self):
        return self.__codigo
   
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor




    @property
    def nombre(self):
        return self.__nombre
   
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
   


    @property
    def precio(self):
        return self.__precio
   
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
   
    def calcular_total(self, unidades):
        return self.precio * unidades


    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)
   
class Pedido:


    def __init__(self, productos, cantidades):
        self._productos = productos
        self._cantidades = cantidades
   
    def total_pedido(self):
        total = 0


        for (p,c) in zip(self._productos, self._cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_pedido(self):
         for (p,c) in zip(self._productos, self._cantidades):
            print("Producto >(", p, "), Cantidad " + str(c))
   
       


p1 = Producto(1, "Producto 1", 5)
p2 = Producto(2, "Producto 2", 10)
p3 = Producto(3, "Producto 3", 20)




print(p1)
print(p2)
print(p3)


print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))



productos = [p1, p2, p3]
cantidades = [5, 10, 2]

pedido = Pedido(productos, cantidades)
print("Total pedido" + str(pedido.total_pedido()))

pedido.mostrar_pedido()
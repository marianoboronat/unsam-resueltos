# alumno mariano boronat
import csv
import fileparse
import json
import informe_final_final

# 11.1
class Lote:
    def __init__(self, nombre, cajones, precio ):
        """representa un lote de cajones de una misma fruta.
        Esta definida de modo que cada instancia de la clase Lote
        (es decir, cada objeto lote) tenga los atributos nombre,
        cajones, y precio."""
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        costo = self.cajones * self.precio
        return costo

    def vender(self, cantidad_venta):
        self.cajones = self.cajones - cantidad_venta
        print(f"se vendieron {cantidad_venta} quedan {self.cajones} cajones")
    
    #11.9 
    def __repr__(self):
        return f"Lote({self.nombre},{self.cajones},{self.precio})"

# 11.11
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'

if __name__ == "__main__":
    # 11.1
    b = Lote('Manzana', 50, 122.34)
    c = Lote('Naranja', 75, 91.75)
    print("precio c:",c.cajones * c.precio)
    print("precio b:",b.cajones * b.precio)

    # 11.2
    s = Lote('Pera', 100, 490.10)
    print(s.costo())
    s.vender(60)

    # 11.3
    camion_dicts = fileparse.parse_csv('../Data/camion.csv',
                                       select = ['nombre', 'cajones', 'precio'],
                                       types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    print(camion)
    print(sum([c.costo() for c in camion]))

    # 11.9
    peras = Lote('Pera', 100, 490.1)
    print(peras)
    
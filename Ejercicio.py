from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str
    
    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0
    
    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1
    
    @property
    def id(self):
        return self.__id
    
    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos
    
    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)
    
    def __add__(self, other):
        if isinstance(other, Conjunto):
            nuevo_conjunto = Conjunto(f"{self.nombre}_UNION_{other.nombre}")
            for elem in self.elementos:
                nuevo_conjunto.agregar_elemento(elem)
            for elem in other.elementos:
                nuevo_conjunto.agregar_elemento(elem)
            return nuevo_conjunto
        else:
            raise TypeError("La operación de unión solo se puede realizar con otro objeto de tipo Conjunto")
    
    def unir(self, otro_conjunto):
        return self + otro_conjunto
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_resultante = f"{conjunto1.nombre}_INTERSECTADO_{conjunto2.nombre}"
        elementos_interseccion = [elem for elem in conjunto1.elementos if elem in conjunto2.elementos]
        nuevo_conjunto = Conjunto(nombre_resultante)
        for elem in elementos_interseccion:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto
    
    def __str__(self):
        elementos_str = ", ".join([elem.nombre for elem in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"


elem1 = Elemento("A")
elem2 = Elemento("B")
elem3 = Elemento("C")


conjunto1 = Conjunto("Conjunto1")
conjunto2 = Conjunto("Conjunto2")


conjunto1.agregar_elemento(elem1)
conjunto1.agregar_elemento(elem2)
conjunto2.agregar_elemento(elem2)
conjunto2.agregar_elemento(elem3)


print(conjunto1.contiene(elem1))  # True
print(conjunto1.contiene(elem3))  # False


union = conjunto1.unir(conjunto2)
print(union)


interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)

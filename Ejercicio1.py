from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str
    
    def __eq__(self, other):
        return self.nombre == other.nombre


class Conjunto:
    contador = 0
    
    def __init__(self, nombre: str):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1
    
    @property
    def id(self) -> int:
        return self.__id
    
    def contiene(self, elemento: Elemento) -> bool:
        return any(e == elemento for e in self.elementos)
    
    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)
    
    def __add__(self, other):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {ot
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in other.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
    def unir(self, otro_conjunto):
        return self + otro_conjunto
    
    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO
        elementos_interseccion = [elemento for elemento in 
        return Conjunto(nombre_conjunto, elementos_intersec
    
    def __str__(self):
        elementos_str = ", ".join([elemento.nombre for elem
        return f"Conjunto {self.nombre}: ({elementos_str})"
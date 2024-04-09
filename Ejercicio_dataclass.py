from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Elemento):
            return NotImplemented
        return self.nombre == other.nombre

class Conjunto:
    contador: int = 0

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        self.elementos: List[Elemento] = []
        Conjunto.contador += 1
        self.__id: int = Conjunto.contador

    @property
    def id(self) -> int:
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento) -> None:
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro: 'Conjunto') -> None:
        for elemento in otro.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro: 'Conjunto') -> 'Conjunto':
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1: 'Conjunto', conjunto2: 'Conjunto') -> 'Conjunto':
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in conjunto1.elementos:
            if elemento in conjunto2.elementos:
                nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __str__(self) -> str:
        nombres_elementos = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({nombres_elementos})"

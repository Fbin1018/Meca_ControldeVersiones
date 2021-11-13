"""
El gerente de la empresa es un empleado que mide 1.80 m, se llama <nombre> y tiene puesto un saco con tres botones.
En este momento el gerente está entrevistando a una persona para su contratación.”
"""

class Persona:
    def __init__(self, nombre, altura, edad):
        self.__altura = altura
        self.__nombre = nombre
        self.__edad = edad

    def getNombre(self):
        return self.__nombre
    def hetEdad(self):
        return self.__edad
    def getaltura(self):
        return self.__altura

    def setEdad(self, nuevaEdad):
        self.__edad=nuevaEdad
    def setNaltura(self, nuevaLtura):
        self.__edad=nuevaLtura


class Empleado(Persona):
    def __init__(self, nombre, altura, edad, cargo):
        super().__init__(nombre, altura, edad)
        self.__cargo = cargo

    def Cargo(self):
        return self.__cargo

    def setCargo(self, nuevoCargo):
        self.__cargo=nuevoCargo



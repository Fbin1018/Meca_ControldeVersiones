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
    def __init__(self, nombre, altura, edad, nivel):
        super().__init__(nombre, altura, edad)
        self.__nivel = nivel

    def Nivel(self):
        return self.__nivel

    def setCargo(self, nuevoNivel):
        self.__nivel=nuevoNivel

class Gerente(Empleado):
    def __init__(self, nombre, altura, edad, nivel, depto):
        super().__init__(self, nombre, altura, edad, nivel)

    def Vestimenta(self):
        print("El gerente tiene puesto un saco con tres botones.")

    def Departamento(self):
        print("El gerente es del departamento de: ")
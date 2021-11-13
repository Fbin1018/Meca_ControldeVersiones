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
        print(self.__nombre)
    def getEdad(self):
        print(self.__edad)
    def getAltura(self):
        print(self.__altura)

    def setEdad(self, nuevaEdad):
        self.__edad = nuevaEdad
    def setAltura(self, nuevaAltura):
        self.__edad = nuevaAltura

    def Presentacion(self):
        print("buenas tardes Gerente, mi nombre es ",self.__nombre,"mucho gusto")


class Empleado(Persona):
    def __init__(self, nombre, altura, edad, nivel):
        Persona.__init__(self, nombre, altura, edad)
        self.__nivel = nivel

    def Nivel(self):
        print(self.__nivel)

    def setNivel(self, nuevoNivel):
        self.__nivel=nuevoNivel


class Gerente(Empleado):
    opcion = 0
    def __init__(self, nombre, altura, edad, nivel, depto):
        Empleado.__init__(self, nombre, altura, edad, nivel)
        self.__depto = depto
        self.__nombre = nombre

    def Introduccion(self):
        print("El gerente de la empresa es un empleado que mide 1.80 m, se llama",self.__nombre, "y tiene puesto un saco con tres botones."
              "\nEn este momento el gerente está entrevistando a una persona para su contratación.")

    def Vestimenta(self):
        print("El gerente", self.__nombre, " tiene puesto un saco con tres botones.")

    def Presentacion(self):
        print("Hola buenas tardes, mi nombre es ",self.__nombre,", soy gerente del departamento de ", self.__depto,""
                "y sere quien le hara su entrevista de trabajo")

    def Problema(self):
        print("Problema: ",self.__nombre)

    def Entrevista(self):
        pass
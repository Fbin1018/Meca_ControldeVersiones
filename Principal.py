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
        print("Buenas tardes Gerente, mi nombre es ",self.__nombre,"mucho gusto")


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
        print(type(self).__name__, ": Le parece si empiezo con una preguntas")
        pregunta1 = "¿Cual es tu nivel de estudios?\n"
        pregunta2 = "¿Cual fue tu ultimo empleo?\n"
        pregunta3 = "¿Has trabajado en el area de Finanzas?\n"
        pregunta4 = "¿Qué Son las Finanzas Corporativas?\n"
        pregunta5 = "¿Que le puedes aportar a esta empresa?\n"

        respuesta3 = "si"
        respuesta4 = "un campo de estudio"

        entrada1 = input(f"pregunta 1 :{pregunta1}")
        entrada2 = input(f"pregunta 2 :{pregunta2}")
        entrada3 = input(f"pregunta 3 :{pregunta3}")
        entrada4 = input(f"pregunta 4 :{pregunta4}")
        entrada5 = input(f"pregunta 5 :{pregunta5}")

        acierto3 = False
        acierto4 = False

        # ////////////////////////////////
        if (entrada3 == respuesta3):
            acierto3 = True
        else:
            acierto3 = False

        if (entrada4 == respuesta4):
            acierto4 = True
        else:
            acierto4 = False

        # /////////////////////////////
        print("Puntaje: ")
        if (acierto3 == True):
            print("1 punto")
        else:
            print("0 puntos")

        if (acierto4 == True):
            print("1 punto")
        else:
            print("0 puntos")

        if(acierto3 == True & acierto4 == True):
            print("Felicidades estas contratado, pasa a RH el dia de mañana empiezas")
        else:
            print("Fue una entrevista muy interesante, pero nosotros te llamamos...")
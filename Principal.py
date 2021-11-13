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
    def __init__(self, nombre, altura, edad, nivel,sueldo):
        Persona.__init__(self, nombre, altura, edad)
        self.__nivel = nivel
        self.__sueldo = sueldo

    def Sueldo(self):
        print(self.__sueldo)

    def setSueldo(self, nuevoSueldo):
        self.__sueldo=nuevoSueldo

    def Nivel(self):
        print(self.__nivel)

    def setNivel(self, nuevoNivel):
        self.__nivel=nuevoNivel


class Gerente(Empleado):
    def __init__(self, nombre, altura, edad, nivel, sueldo, depto):
        Empleado.__init__(self, nombre, altura, edad, nivel, sueldo)
        self.__depto = depto
        self.__nombre = nombre

    def Introduccion(self):
        print("El gerente de la empresa es un empleado que mide 1.80 m, se llama",self.__nombre, "y tiene puesto un saco con tres botones."
              "\nEn este momento el gerente está entrevistando a una persona para su contratación.")

    def Vestimenta(self):
        print("El gerente", self.__nombre, " tiene puesto un saco azul con tres botones"
                                           "ademas usa una corbata roja")

    def Presentacion(self):
        print("Hola buenas tardes, mi nombre es ",self.__nombre,", soy gerente del departamento de ", self.__depto,""
                "y sere quien le hara su entrevista de trabajo")

    def Problema(self):
        print("Problema: ",self.__nombre)

    def Entrevista(self):
        print(type(self).__name__,": Le parece si empiezo con una preguntas")
        pregunta1 = "¿Su nivel de estudios es superior a Bachiller?\n"
        pregunta2 = "¿Cuenta con titulo Universitario?\n"
        pregunta3 = "¿Cual fue tu ultimo empleo?\n"
        pregunta4 = "¿Has trabajado en el area de Finanzas?\n"
        pregunta5 = "¿Qué Son las Finanzas Corporativas?\n"
        pregunta6 = "¿Que le puedes aportar a esta empresa?\n"

        respuesta1 = "si"
        respuesta2 = "si"
        respuesta4 = "si"
        respuesta5 = "un campo de estudio"

        entrada1 = input(f"pregunta 1 :{pregunta1}")
        entrada2 = input(f"pregunta 2 :{pregunta2}")
        entrada3 = input(f"pregunta 3 :{pregunta3}")
        entrada4 = input(f"pregunta 4 :{pregunta4}")
        entrada5 = input(f"pregunta 5 :{pregunta5}")
        entrada6 = input(f"pregunta 6 :{pregunta6}")

        acierto1 = False
        acierto2 = False
        acierto4 = False
        acierto5 = False

        #////////////////////////////////
        if(entrada1 == respuesta1):
            acierto1 = True
        else:
            acierto1 = False

        if (entrada2 == respuesta2):
            acierto2 = True
        else:
            acierto2 = False

        if (entrada4 == respuesta4):
            acierto4 = True
        else:
            acierto4 = False

        if (entrada5 == respuesta5):
            acierto5 = True
        else:
            acierto5 = False

        #/////////////////////////////
        if (acierto1 == True):
            print("1 punto")
        else:
            print("0 puntos")

        if (acierto2 == True):
            print("1 punto")
        else:
            print("0 puntos")

        if (acierto4 == True):
            print("1 punto")
        else:
            print("0 puntos")

        if (acierto5 == True):
            print("1 punto")
        else:
            print("0 puntos")

        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if (acierto1 == True & acierto2 == True & acierto4 == True & acierto5 == True):
            print("Felicidades estas contratado, pasa a RH el dia de mañana empiezas")

        elif (acierto1 == True & acierto2 == True & acierto4 == True):
            print("Felicidades estas contratado, pasa a RH el dia de mañana empiezas")

        elif (acierto1 == True & acierto2 == True):
            print("Fue una entrevista muy interesante, pero nosotros te llamamos...")

        elif (acierto1 == True):
            print("Fue una entrevista muy interesante, pero nosotros te llamamos...")
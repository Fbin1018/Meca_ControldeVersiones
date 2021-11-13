
import Principal as main_Principal
"""
El gerente de la empresa es un empleado que mide 1.80 m, se llama <nombre> y tiene puesto un saco con tres botones.
En este momento el gerente está entrevistando a una persona para su contratación.
"""

gerente = main_Principal.Gerente(input("nombre del Gerente: "),1.80, 39, 5, "Finanzas")
gerente.Problema()
print("")
gerente.Introduccion()
print("")
gerente.Presentacion()
persona = main_Principal.Persona(input("ingrese su nombre: "),1.82, 32)
persona.Presentacion()
print("")
gerente.Entrevista()
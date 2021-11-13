
import Principal as main_Principal
"""
El gerente de la empresa es un empleado que mide 1.80 m, se llama <nombre> y tiene puesto un saco con tres botones.
En este momento el gerente está entrevistando a una persona para su contratación.
"""

gerente = main_Principal.Gerente("Gerardo",1.80, 39, 5, "Finanzas")
gerente.Problema()
gerente.Introduccion()
gerente.Presentacion()
gerente.Entrevista()
persona = main_Principal.Persona("Jose", 1.78, 30)
persona.getNombre()
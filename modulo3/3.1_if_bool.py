'''
Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

Imprima el enunciado "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" 
en la pantalla si la cadena ingresada es "ESPATIFILIO".
Imprima "No, ¡quiero un gran ESPATIFILIO!" si la cadena ingresada es "espatifilo".
Imprima "¡ESPATIFILIO!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.
'''

name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("!ESPATIFILIO!, ¡No", name + "!")

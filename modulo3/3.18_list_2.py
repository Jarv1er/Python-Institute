'''
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

Tu tarea es:

Escribir una línea de código que solicite al usuario que reemplace el número central en la lista 
con un número entero ingresado por el usuario (Paso 1).
Escribir una línea de código que elimine el último elemento de la lista (Paso 2).
Escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
'''

hat_list = [1, 2, 3, 4, 5]  

user_number = int(input("Ingresa un numero: ")) 
hat_list[2] = user_number

hat_list[-1]

print(len(hat_list))

print(hat_list)

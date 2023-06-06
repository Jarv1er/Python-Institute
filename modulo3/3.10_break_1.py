'''
Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra 
a menos que ingrese "exit" como la palabra de salida secreta, en cuyo caso el mensaje 
"¡Has dejado el bucle con éxito". Debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. 
Utiliza el concepto de ejecución condicional y la sentencia break.
'''

palabra = input("Ingresa una palabra: ")

while palabra != "exit":
    palabra = input("Ingresa una palabra: ")
    if palabra == "exit":
        break
print("¡Has dejado el bucle con éxito")
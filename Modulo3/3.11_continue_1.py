'''
Pedir al usuario que ingrese una palabra.
Utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.

Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales
 A , E , I , O , U de la palabra ingresada.

Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.

'''

word = input("Ingresa una palabra: ")
user_word = word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)


# Entrada de muestra: Gregory
# Salida esperada:
# G
# R
# G
# R
# Y

# Entrada de muestra: abstemious
# Salida esperada:
# B
# S
# T
# M
# S
# Entrada de muestra: IOUEA
# Salida esperada:

 
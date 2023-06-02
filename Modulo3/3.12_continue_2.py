'''
Pedir al usuario que ingrese una palabra.
Utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; 
hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.

Emplea la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
Asigne las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.

Analiza el código en el editor. Hemos creado word_without_vowels y le hemos asignado una cadena vacía. 
Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas 
en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.
'''

word_without_vowels = ""

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
        word_without_vowels += letter

print(word_without_vowels)

# Entrada de muestra: Gregory
# Salida esperada: GRGRY

# Entrada de muestra: abstemious
# Salida esperada: BSTMS

# Entrada de muestra: IOUEA
# Salida esperada:

 
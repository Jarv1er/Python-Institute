# Modulo 3 Bucles

odd_number = 0
even_numbers = 0

number = int(input("Inserta un numero o escribe 0 para detener: "))

while number != 0:
    if number % 2 == 1:
        odd_number += 1
    else:
        even_numbers += 1

    number = int(input("Inserta un numero o escribe 0 para detener: "))

print("Cuenta de números impares:", odd_number)
print("Cuenta de números pares:", even_numbers)
print()
# ===============================================

print("Contador")
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
# ===============================================
# el mismo resultado pero mas compacto 
# counter = 5
# while counter:  <-- Mientras sea True (0 pasara a ser False)
#     print("Dentro del bucle.", counter)
#     counter -= 1
# print("Fuera del bucle.", counter)
'''
Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" 
hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final 
"¡Listos o no, ahí voy!"
'''

import time

for i in range(1, 6):
    print(i, "Mississippi")
    segundos = time.sleep(1)

print("¡Listos o no, ahí voy!")



print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# Puntos Clave 1
# =========================== 1
print("Ejercicio 1")

x = 5
y = 10
z = 8

print(x > y)  # False
print(y > z)  # True
print()
# =========================== 2
print("Ejercicio 2")

x, y, z = 5, 10, 8

print(x > z)  # False
print((y - 5) == x)  # True
print()
# =========================== 3
print("Ejercicio 3")

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)  # True
print((y - 5) == x)  # False
print()
# =========================== 4
print("Ejercicio 4")

x = 10

if x == 10:
    print(x == 10)  # True
if x > 5:
    print(x > 5)  # True
if x < 10:
    print(x < 10)  
else:
    print("else")  # else
print()
# =========================== 5
print("Ejercicio 5")

x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int(x) > 1:
        print("dos")
    elif int(x) < 1:
        print("tres")
    else:
        print("cuatro")  # cuatro
if int(x) == 1:
    print("cinco")  # cinco
else:
    print("seis")
print()
# =========================== 6
print("Ejercicio 6")

x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")  # uno
if y == int(z):
    print("dos")  # dos
elif x == y:
    print("tres")  # no se ejecita porque es un elif si fuera un if si 
else:
    print("cuatro")  # no se ejecuta porque el segundo if es True

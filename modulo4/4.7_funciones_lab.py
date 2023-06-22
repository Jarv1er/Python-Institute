'''
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

¿Complicado? De ningúna manera. Por ejemplo, 8 no es un número primo, ya que puedes dividirlo 
entre 2 y 4 (no podemos usar divisores iguales a 1 y 8, ya que la definición lo prohíbe).

Por otra parte, 7 es un número primo, ya que no podemos encontrar ningún divisor para el.
Tu tarea es escribir una función que verifique si un número es primo o no.
'''

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# 2 3 5 7 11 13 17 19
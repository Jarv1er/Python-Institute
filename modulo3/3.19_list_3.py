# Dicha operación se realiza mediante un método llamado append(). 
# Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

# La longitud de la lista aumenta en uno.

# El método insert() es un poco más inteligente: puede agregar un nuevo elemento en cualquier 
# lugar de la lista, no solo al final.


numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)


my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)


# Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos) 
# y luego agregar nuevos elementos según sea necesario.

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

my_list = [10, 1, 8, 3, 5]
total = 0
print()

# Pero el bucle for puede hacer mucho más. Puede ocultar todas las acciones conectadas a la indexación 
# de la lista y entregar todos los elementos de la lista de manera práctica.

for i in range(len(my_list)):
    total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)
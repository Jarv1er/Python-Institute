# Indexando Listas

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111  # Imprimiendo contenido de la lista con 111.
print("\nContenido de la lista con cambio: ", numbers)  # Contenido de la lista actual.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("\nContenido de la lista con intercambio:", numbers)  # Imprimiendo el contenido de la lista actual.

print(numbers[0])  # Accediendo al primer elemento de la lista.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

# No puedes acceder a un elemento que no existe , no puedes obtener su valor ni asignarle un valor. 
# Ambas instrucciones causarán ahora errores de tiempo de ejecución:

print(numbers[4])  # IndexError: list index out of range
numbers[4] = 1  # IndexError: list index out of range

# Los índices negativos son válidos y pueden ser muy útiles.
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
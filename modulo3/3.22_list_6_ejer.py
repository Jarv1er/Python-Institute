'''
Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

Paso 1: Crea una lista vacía llamada beatles.

Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: 
John Lennon, Paul McCartney y George Harrison.

Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue 
los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.

Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.

Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
'''

Beatles = []
print("Paso 1:", Beatles)

Beatles.append("Jonh Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

for a in range(2):
    Beatles.append(input("Agrega un miembro de la banda a la lista: "))
print("Paso 3:", Beatles)

del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)

Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))

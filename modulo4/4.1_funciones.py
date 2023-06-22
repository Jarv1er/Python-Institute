print("================================== 1")

# Paso de parametros posicionales
def introducion(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introducion("Javier", "Palomo")
introducion("Luke", "Skywalker")
introducion("Jesse", "Quick")

print("================================== 2")

# Paso de Argumentos con palabra clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

print("================================== 3")

# Combinar argumentos posicionales y de palabra clave
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)

print("================================== 4")

# Funciones parametrizadas: mas detalles
def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Pérez")
introduction("Enrique")
introduction(first_name="Guillermo")

print("================================== 5")

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction()
introduction(last_name="Rodríguez")



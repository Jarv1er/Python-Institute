# Un ejemplo de una función de tres parámetros:

def address(street, city, postal_code):
    print("Tu dirección es:", street, city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")

address(s, c, p_c)
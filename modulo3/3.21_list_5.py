# Ahora puedes intercambiar fácilmente los elementos de la lista para revertir su orden:

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# 5, 3, 8, 1, 10, 

# ¿Puedes usar el bucle for para hacer lo mismo automáticamente, 
# independientemente de la longitud de la lista? Si, si puedes.

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2): # 5//2 = 2
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)                            

# my_list[length - i - 1]  - Recorre la lista desde el ultimo elemento hasta 2 (mira el range)
# my_list[i]  -Recorre los 2 primeros elementos de la list
 


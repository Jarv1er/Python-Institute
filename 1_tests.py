for i in range(10):
    print("El valor de i es actualmente", i)

for i in range(2, 8):
    print("El valor de i es actualmente", i)

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

counter = 5
while counter > 2:
    print(counter)
    counter -= 1

word = "Python"
for letter in word:
    print(letter, end="*")

for i in range(1, 10):
    if i % 2 == 0:
        print(i)


text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text2 = "pyxpyxpyx"
for letra in text2:
    if letra == "x":
        continue
    print(letra, end="")


n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

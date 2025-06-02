lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)
print(lista2)
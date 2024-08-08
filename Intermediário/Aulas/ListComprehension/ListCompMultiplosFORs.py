lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))#Para colocar mais valores em um único indice de lista, é preciso usar ferramentas que permitam incluir esse valores multiplos, como a tupla
print(lista)

lista_comp = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista_comp)
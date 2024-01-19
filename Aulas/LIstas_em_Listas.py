'''
Lista de listas e seus índices
'''

salas = [
    # 0      1
    ['Maria', 'Helena',], #0
    #0
    ['Elaine',], #1
    #0    1    2
    ['Luiz', 'João', 'Eduarda', [0, 10, 20, 30, 40]], #2
]

print(salas[0][1])
#Primeiro indice é referente a posição da lista maior, o segundo pega o valor na lista menor

print(salas[2][3][2])
#Agora, descemos mais um escala de hierarquia para pegar o valor 20

#Ou podemos usar por for
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
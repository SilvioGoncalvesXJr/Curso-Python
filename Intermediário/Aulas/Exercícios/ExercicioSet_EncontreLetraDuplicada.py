'''
Crie uma função que encontra o primeiro duplicados considerando o segundo número como a duplicação, Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o números duplicado em si.
    Ex.:
    [1,2,3,3,2,1] -> 1, 2 e 3 são duplicados (retorne 3 como primeiro digito, seguido do 2 e 1)
    [1,2,3,4,5,6] -> Retorne -1 (não tem duplicados)
    
    Se não achar duplicados na lista, retorne -1
'''

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def analise (lista):
    controle = set()
    repetidos = set()
    for item in lista:
        if item in controle:
            repetidos.add(item)
        else:
            controle.add(item)
    if len(repetidos) == 0:
        return "-1"
    else:
        return set(repetidos)
            

for lista in lista_de_listas_de_inteiros:
    resultado = analise(lista)
    if resultado == "-1":
        print(f'Após análise da {lista}, verificou-se que a mesma não se repete, resultando no valor de {resultado}')
    else:
        print(f'Após análise da {lista}, tais números se repetiram {resultado}')
#NÃO ESTOU CONSEGUINDO COLOCAR NA ORDEM CERTA OS VALORES DO PRIMEIRO QUE SE REPETE, SEGUIDO PELOS DEMAIS
# ----------------------------------------------------------------------------------------------------------------------------

def encontrar_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontrar_primeiro_duplicado(lista)
    )


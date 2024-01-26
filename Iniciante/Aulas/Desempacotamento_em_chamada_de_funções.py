#Desempatotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1,2,3, 'Eduarda']
tupla= 'Python', 'é', 'legal'
salas = [
    # 0      1
    ['Maria', 'Helena',], #0
    #0
    ['Elaine',], #1
    #0    1    2
    ['Luiz', 'João', 'Eduarda', [0, 10, 20, 30, 40]], #2
]


"""
Podemos realizar o desempacotamento das chamadas das funções, que ao invés de fazer um for para realizar, podemos aplicar diretamente
no print, usando o '*', deixando-os na mesma linha de output
"""
for nome in lista:
    print(nome, end=' ', sep='')

#Podemos fazer a mesma coisa, mas usando o print apenas
print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n') #Faz com que quebre a linha na separação, ficando mais organizado

# -------------------------------------------------------------------------------------------

"""
No caso da lista, os números dentro dela podem dar problema, quando quiser pegar a ultima string, por exemplo.
Assim, podemos usar delimitadores para isso, com o '*_' que seignifica pegar o resto
"""

# primeiro, b, *_, ultimo = lista
# print(primeiro, ultimo)
# """Aqui, mesmo depois do b, o resto empacota tudo e armazena. Porém, é possível adicionar uma nova variável, que pegará 
# o último valor. A lógica é, faz a associação das variáveis com os itens da lista, e a ultima, depois do resto, só pega
# o ultimo valor e assim por diante
# """
# primeiro, b, *_, antipenultimo, ultimo = lista
# print(primeiro, ultimo, antipenultimo)


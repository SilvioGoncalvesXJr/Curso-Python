"""
Utilziar o metodo 'return' faz com que você retorne um valor específico tratado dentro de uma função para ser
utilizado em operações fora do escopo da mesma, como o resultado da soma de dois inteiros, para depois pegar-lo e 
realizar novas operações com o mesmo

OBS.: Importante dizer que 'print' e 'return' não tem nada a ver uma coisa com a outra, a primeira apenas apresenta um resultado
e não a devolve para fora do escopo, o que daria um tipo 'None' se tentasse

OBS.: Se colocar linhas de código após um 'return' dentro da função, essas não serão lidas. Como se desse um
break na função. Mas podem ter mais de 1 'return' em uma função, desde que estejam dentro de condicionais ou um em condicional
e outro fora, por exemplo
"""

def soma(x, y):
    if x > 10:
        return 10
    return x + y

soma1= soma(2,2)
soma2 = soma(3,3)
print(soma1 + soma2)
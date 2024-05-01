"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
Naõ temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno

As funções possuem escopos particulares, de forma que, de modo geral, as suas atividades que ocorrem dentro dela não são propriamente 
repassadas para o código de fora. Mas existem algumas formas de quebrar isso, como usando o "global", como visto abaixo.
Ele faz com que a variável também seja levada para fora do escopo da função

Se por acaso não colocar o 'global' a comentar o 'x' da função 'outra_funcao', ele irá pegar o x mais próximo, que
seria o definido no começo da função 'escopo'. E se comentar tbm este, pegar o x = 1.
Isso só porde quando é feito do escopo de dentro para fora, e não de fora para dentro, caso o print de y seja colocado
em qualquer lugar fora de outra função, mesmo sendo estabelecido ali, irá dar erro.
"""

x = 1


def escopo():
    global x
    x = 10
    print(x)

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
#Mudou o valor por causa do global atribuido dentro da função
print(x)
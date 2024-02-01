"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados

As funções possuem escopos particulares, de forma que, de modo geral, as suas atividades que ocorrem dentro dela não são propriamente 
repassadas para o código de fora. Mas existem algumas formas de quebrar isso, como usando o "global", como visto abaixo.
Ele faz com que a variável também seja levada para fora do escopo da função
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
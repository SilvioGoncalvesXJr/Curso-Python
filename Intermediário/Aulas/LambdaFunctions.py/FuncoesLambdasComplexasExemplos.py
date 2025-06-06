def executa(funcao, *args): #É recomendado criar uma função de execução para as funções lambdas, ao invés de executar diretamente
    return funcao(*args)

#Função lambda é para coisas rápidas e fáceis. Se almentar a complexidade já fica confuso


def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

#Transformar em Lambda Functions

print(
    executa(
        lambda x,y: x + y, 2, 3
    ),
    executa(soma, 2, 3),
    soma(2, 3)
)#diferentes formas de escrever a mesma função

duplica = executa(
    lambda m: lambda n: m * n, 2 #Pega a primeira função 'cria_multiplicador', o segundo lambda é a função interna 'multiplica', retornando a mutiplicação dos dois
)

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8
    )
)#outro modo de usar o soma
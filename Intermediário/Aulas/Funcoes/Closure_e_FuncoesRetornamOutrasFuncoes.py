'''
Closure ocorre quando você quer que uma função seja executada, mas em um momento posterior, deixando-a salva na memória, com os parametros
já estabelecidos, para depois, só chamar e finalmente executar, como podemos ver:
'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar
#Aqui, se estivesse 'saudar()' assim que chamasse criar_saudacao iria chamar e executar tbm a outra. Deixando assim,
#ela apenas retorna a função para uma variável, armazenando-a e os valores de saudacao e nome, para executar depois

s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa noite', 'Maria')

print(s1())
print(s2())
#Aqui, colocamos 's1()' e 's2()' por ser a sintaxe de um closure, para fechar a função e a executá-la

#Função que chama outra função. Outra forma, que deixa mais organizada e funcional é da seguinte forma:

def criar_saudacao1(saudacao1):
    def saudar1(nome1):
        return f'{saudacao1}, {nome1}'
    return saudar1

falar_bom_dia = criar_saudacao1('Bom dia')
falar_boa_noite = criar_saudacao1('Boa noite')

for nome1 in ['Maria', 'João', 'Pedro']:
    print(falar_bom_dia(nome1))
    print(falar_boa_noite(nome1))
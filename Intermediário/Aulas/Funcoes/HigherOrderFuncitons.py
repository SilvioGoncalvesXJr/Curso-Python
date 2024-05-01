"""
É possível passar funções como argumentos de outras funções. E, além disso, chamar uma função dentro de outra, e o seu resultado
retornar para a função primeira.
Observando a ordem de preferência das funções
"""

def saudacao (msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): #Esse args está empacotando, pegando todos os valores que forme passados como parametro depois de funcao
    return funcao(*args)#Aqui desempacota, de modo a poder pegar os parametros certos da funcao saudacao sem erros

print(
    executa(saudacao, "Bom dia", "Luiz")
)

print(
    executa(saudacao, "Boa noite", "Maria")
)
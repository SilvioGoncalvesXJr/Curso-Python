"""
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como parâmetro
"""
import os

# def multiplcacao(valor):
#     def duplicao():
#         duplicado = valor * 2
#         return duplicado

#     def triplicar():
#         triplicado = valor * 3
#         return triplicado
    
#     def quadruplicar():
#         quadruplicado = valor * 4
#         return quadruplicado
    
#     return duplicao#, triplicar, quadruplicar

def multiplicacao(valor, multiplicador):
    def operacao():
        resultado = valor * multiplicador
        return resultado
    return operacao

flag = 0
while flag == 0:
    try:
        numero = int(input('Favor, informar um número diferente de 0: \n'))
    except:
        print("Precisa ser um número diferente de 0. Informe novamente")
        os.system('cls')
        continue
    if numero == 0:
        print("O número não pode ser 0. Favor, escolher outra opção")
        os.system('cls')
    else: 
        flag = 1

duplicacao = multiplicacao(numero, 2)
triplo = multiplicacao(numero, 3)
quadro = multiplicacao(numero, 4)
print(f'O resultado da duplicação de {numero} é {duplicacao()}\nO seu triplo é {triplo()}\nAgora o seu quadruplo é {quadro()}')




    
    
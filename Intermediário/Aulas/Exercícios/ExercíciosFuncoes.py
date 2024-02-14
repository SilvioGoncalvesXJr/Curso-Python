'''
Crie uma função que multiplica todos os argumentos não nomeados recebidos e retorne o total para uma variável e a mostre
Crie outra função que fala se um número é par ou ímpar. Retorne o resultado
'''
flag = '0'
sequencia = []

while flag == '0':
    entrada = input('Deseja informar algum número para tratamento: 1 para sim, 2 para não \n')
    if entrada == '1':
        numero = int(input('Informe o número: '))
        if numero == 0:
            print('Não pode escolher o número 0. Escolha outro')
        else:
            sequencia.append(numero)
    elif entrada == '2':
        flag = '1'
    else:
        print('Escolha uma opção válida')

def multiplicacao(*args):
    total = 1
    for i in args:
        total *= i
    return total

def par_impar(resultadoMulti):
    verificar = resultadoMulti % 2
    resultado = ''
    if verificar == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    
    return resultado

resultadoMulti = multiplicacao(*sequencia)
par_ou_impar = par_impar(resultadoMulti)
print(f'A sequencia de números {sequencia} multiplicado deu {resultadoMulti} e é {par_ou_impar}')

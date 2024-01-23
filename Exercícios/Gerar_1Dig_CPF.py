"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

lista = []
listaint = []
listaintAtt = []

cpf = input("Informe um cpf válido: ")


for i in cpf:
    lista.append(i)
print(lista)

for i in lista:
    if i == '.' or i == '-':
        lista.remove(i)
print(lista)

lista.pop()
lista.pop()

for i in lista:
    listaint.append(int(i))
print(listaint)

valor = 10
for i in listaint:
    listaintAtt.append(i*valor)
    valor -= 1
print(listaintAtt)

valores = 0
for i in listaintAtt:
    valores += i
print(valores)

valores = valores * 10
print(valores)

valores = valores % 11
print(valores)

primeiro_digito = 0 if valores > 9 else valores

print(f'O primeiro dígito é {primeiro_digito}')

# del lista[3]
# print(lista)
# del lista[6]
# print(lista)
# del lista[9]
# print(lista)
# cpf_separado = cpf.split('.') 
# divisao_travessao = cpf_separado.pop(2)
# divisao_travessao = divisao_travessao.split('-')

# for i in divisao_travessao:
#     cpf_separado.append(i)
# print(cpf_separado)

# for i in cpf_separado:
#     lista.append(int(i))
# print(lista)


#---------------------------------------------------------------------------------------------------
#Solução Professor
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
print(digito_1)
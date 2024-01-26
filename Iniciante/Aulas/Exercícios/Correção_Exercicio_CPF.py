'''Meios de fazer, caso tenha elementos no cpf que não sejam números'''
#Pode resolver usando o replace ou usando expressão regular
# cpf_enviado_usuario = '06569376373'

import re, sys

entrada = input('Informe CPF')
# cpf_enviado_usuario = cpf_enviado_usuario.replace('.','')\
#     .replace('-','')\
#     .replace(' ','')

cpf_enviado_usuario = re.sub(
    r'[^0-9]', #Substitui tudo que não estiver no range de números de 0 a 9
    '', #substitui por o parâmetro passado aqui
    entrada #Posso colocar varios elementos aleatorios que tirará e deixará so os numeros
)
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

#Outro problema a ser solucionado é se o usuário mandar dados sequenciais, que pode passar como válido, mas é um erro
entrada_e_sequencial = entrada == entrada[0] * len(entrada)
#Ver ser é uma sequencia

if entrada_e_sequencial:
    print("Você enviou dados sequenciais")
    sys.exit()

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
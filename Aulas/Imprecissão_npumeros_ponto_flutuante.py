"""
Quando trabalhamos com pontos flutuantes, algumas vezes, ocorre imprecissões de resulta,
não só no python, mas como em outras linguagens.
Veremos alguns jeitos de contornar 
Double-precision floating-point format IEEE 754
"""
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

#Podemos usar as F-String, que retorna um type string, como nome diz
#onde podemos delimitar as casas decimais
print(f'{numero_3:.2f}')

#Ou podemos usar a função round(), que retorna um float e arredonda os valores
#Depois da virgula, colocamos o tato de casa, mas se for zero, ele desconsidera
print(round(numero_3, 2))

#Por fim, podemos usar a lib decimal, só que é mais para quando
#precisamos trabalhar com precissões com números float muito grandes
numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5
print(numero_6)


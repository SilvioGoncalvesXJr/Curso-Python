"""
args - Serve como elemento de empacotamento de elementos, 
para trabalhar dentro de uma função, evitando que erros sejam especificados
podendo passar quando elementos não nomeados quiser
como no exmelo de:
def soma (x,y):
    return x + y

soma(1, 2, 3, 4, 5)
Isso dará erro por causa da quantidade de paramentors estipulados
"""
#Importante lembrar do desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)
#Vai salvar o 3 e 4 no resto, para depois eu manipular caso queira
#Você também pode usar em uma variável do tipo tupla, para pegar apenas seus elementos
numeros = 1,2,3,4,5,5,6,7,7,8
print(type(numeros))
print(numeros)
print(*numeros)
#Este desempacota, deixando apenas os valores. E com isso, pode trabalhar de outras formas, como verá abaixo

#Agora o arg

def soma(*args):
    total = 0
    #Flag de acumulador, para controle
    for numero in args:
        total += numero
    return total

soma123 = soma(1, 2, 3)
print(soma123)

soma456 = soma(4,5,6)
print(soma456)


outraSoma = soma(1,23,4,6,7,565,6434,32)
print(outraSoma)

numerossss = 1,2,3,4,5,5,6,7,7,8
# testeSoma = soma(numerossss) #Dará erro pois ira empacotar de novo, tupla dentro de outra tupla, dando problema
#para resolver, basta usar o desempacotamento e funcionará
testeSoma = soma(*numerossss)
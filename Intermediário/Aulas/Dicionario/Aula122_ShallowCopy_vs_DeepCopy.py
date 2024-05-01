#Quando se quer copiar um dicionário é importante prestar atenção.
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

#d1 = d2 Se fizermos isso, não estamos copiando e sim, realizando uma indicação,
#de modo que se alterar valores de d2, também modificará d1.
#Para evitar isso, podemos usar o Shallow copy e o Deep Copy

#d2 = d1.copy()
#d2['c1'] = 1000
#d2['l1'] = 99999
#print(d2)
#Esse é o Shallow Copy, que realiza a copia de forma raza, deixando d2 parcialmente indenpendete.
#Ele copia os valores imutaveis de d1 para d2 de forma independente, mas o multáveis continua como apenas indicador, o caso da lista)
#de forma a que se alterar d2, modifica d1. Para evitar isso, usamos o Deep Copy

#No Deep Copy, ele copia tudo e deixa totalmente independente. Para aplicar, precisamos importar 
#a biblioteca 'copy'

d2 = copy.deepcopy(d1)
d2['c1'] = 1000
d2['l1'] = 99999
print(d1)
print(d2)
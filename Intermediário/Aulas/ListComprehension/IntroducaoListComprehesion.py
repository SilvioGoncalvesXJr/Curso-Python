'''
List Comprehesion em Python é uma forma rápida para criar listas
a partir de iteráveis
Iremos mostrar alguns métodos de fazer a mesma ação e depois usando a list comprehension
'''
print(list(range (10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista_list_comp = [numero for numero in range (10)]
#Aqui, os termos antes do for serão o ponto de controle e mecanismo de ação. No caso, irá adicionar numero na lista
print(lista_list_comp)

lista_lista = [numero * 2 for numero in range (5)]
print(lista_lista)
#Métodos em intancias de classes Python
#Hard coded - É algo que foi escrito diretamento no código

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando')

fusca = Carro('Fusca')
fusca.acelerar()

gurgel = Carro('Gurgel')
gurgel.acelerar()
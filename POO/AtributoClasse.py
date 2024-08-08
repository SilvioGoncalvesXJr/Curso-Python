class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
#Pessoa.ano_atual = 1 Dessa forma, seria capaz de alterar o valor do atributo de classe mesmo fora do escopo, atrapalhando todas as outras execuções
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
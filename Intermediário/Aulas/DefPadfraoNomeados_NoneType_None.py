"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)
#Normalmente, ao chamar uma função, precisa passar todos os parâmetros, mas se não quiser, terá que fazer desta forma, atribuindo None
#Da mesma forma das funções de argumentos nomeados, se nomear um, todos os seguintes precisar ser tbm. Aqui é da mesma forma
def soma2(x, z=None, y=None):
    if z and y is not None:
       print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print("Hello")
        # print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)

soma2(1, 2)
soma2(3, 5)
soma2(100, 200)
soma2(7, 9, 0)
soma2(y=9, z=0, x=7)
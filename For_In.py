"""
Na questão de loops, o while é mais voltado para quando
não se sabe exatamente quantos loops serão dados,
mas caso seja de fácil percepção, como o tamanho de uma string,
é mais adequado e fácil tbm usar o for
"""

texto = "Python"
novo_texto = ""

for letra in texto:
    novo_texto += f"{letra}*"
    print(letra)
print(novo_texto)
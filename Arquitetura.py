# Questão 3.14.6 de Arquitetura de Computadores - Silvio Gonçalves

import math
import numpy as np

# Cálculo da raiz quadrada de 10
raiz_quadrada = math.sqrt(10)

# Cálculo do resultado
resultado = raiz_quadrada * raiz_quadrada

# Conversão para precisão simples (float32)
precisao_simples = np.float32(resultado)

# Conversão para precisão dupla (float64)
precisao_dupla = np.float64(resultado)

print("Resultado em precisão simples (float32):", precisao_simples)
print("Resultado em precisão dupla (float64):", precisao_dupla)
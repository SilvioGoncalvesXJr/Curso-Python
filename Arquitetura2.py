# Questão 3.12.2 Arquitetura de computadores - Silvio Gonçalves

import struct
import sys
import math

def checa_overflow(resultado):
    max_value = sys.float_info.max
    if resultado == float('inf') or resultado > max_value:
        return True
    return False

def checa_underflow(resultado):
    min_value = sys.float_info.min
    if resultado == 0.0 or resultado < min_value:
        return True
    return False

def converter_em_IEE754(N):
    packed = struct.pack('!f', N)
    
    bits = ''.join(bin(byte).replace('0b', '').rjust(8, '0') for byte in packed)
    
    sinal = bits[0]
    expoente = bits[1:9]
    mantissa = bits[9:]
    
    return sinal, expoente, mantissa

def padroniza_em_IEE_754(sinal, expoente, mantissa):
    bits = sinal + expoente + mantissa
    
    byte_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]
    
    packed = bytes(int(chunk, 2) for chunk in byte_chunks)
    
    numero = struct.unpack('!f', packed)[0]
    
    return numero

A = 3.14
B = 2.34
print('A')
sinal, expoente, mantissa = converter_em_IEE754(A)
print(f'Sinal: {sinal}')
print(f'Expoente: {expoente}')
print(f'Mantissa: {mantissa}')

numero_convertido = padroniza_em_IEE_754(sinal, expoente, mantissa)
print(f'Número convertido: {numero_convertido}')
print(" ")
print('B')
sinal, expoente, mantissa = converter_em_IEE754(B)
print(f'Sinal: {sinal}')
print(f'Expoente: {expoente}')
print(f'Mantissa: {mantissa}')

numero_convertido = padroniza_em_IEE_754(sinal, expoente, mantissa)
print(f'Número convertido: {numero_convertido}')
print(' ')
print('produto de A e B')
sinal, expoente, mantissa = converter_em_IEE754(A*B)
print(f'Sinal: {sinal}')
print(f'Expoente: {expoente}')
print(f'Mantissa: {mantissa}')
resultado_arredondado = round(A*B, sys.float_info.mant_dig)
if checa_overflow(resultado_arredondado):
    print("ocorreu overflow")
if checa_underflow(resultado_arredondado):
    print("ocorreu underflow")
else:
    print("sem underflow ou overflow!")
numero_convertido = padroniza_em_IEE_754(sinal, expoente, mantissa)
print(f'Número convertido: {numero_convertido}')
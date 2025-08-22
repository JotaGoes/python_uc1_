##
# DESAFIO 1 FEITO (inicio da aula)
##

##
# 2 soma de matrizes = tive duvidas, parei no meio do código, realizar estudos sobre operações em matrizes
##

import random

matriz = []
for i in range(4):
    linha= []
    for j in range(4):
        elemento=(random.randint(1,100))
        linha.append(elemento)
    matriz.append(linha)

matriz2 = []
for i in range(4):
    linha= []
    for j in range(4):
        elemento=(random.randint(1,100))
        linha.append(elemento)
    matriz2.append(linha)

resultado=matriz[i][j]+matriz2[i][j]

print(f"{matriz}")
print(f"{matriz2}")
print(f"A soma das duas matrizes é de : {matriz2}")
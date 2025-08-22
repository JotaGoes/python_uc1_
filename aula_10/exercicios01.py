##
# MATRIZES
# 21/08/2025
##

##
# Matriz 3x3 - FUNCIONANDO
##

#matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]

#print("Elemento (0,0):", matriz[0][0])  # O primeiro 0 remete à primeira linha da matriz, já o segundo, à primeira casa dessa linha
#print("Elemento (2,1):", matriz[2][1])  # O 2 remete à terceira linha da matriz, já o 1, à segunda casa dessa linha

#for linha in matriz:
#    print(f"{linha}")



##
# Matriz aleatória - FUNCIONANDO
##
#matriz2= []
#for i in range(3) :
#    linha = []

#    for j in range (3) :
#        #linha.append(i)
#        #linha.append(j)
#        elemento = random.randint(0,100)
#        linha.append(elemento)
#    matriz2.append(linha)

    #ou, pode se fazer:
    #linha.append(random.randint(0,100))

#for linha in matriz2:
#    print(f"{linha}")

#for linha in matriz2:
#    for elemento in linha:
#        print(f"{elemento:02}", end=' ') #usar o :02 para a impressão ficar com dois dígitos, aqueles que houverem um, ficarão com o 0 na frente
#    print(f" ")

##
# dois laços for (estilo de outras linguagens: PHP, Java, JavaScript, C, C++) - FUNCIONANDO
##
    
#for i in range(3):
#    for j in range(3):
#        print(f"Elemento ({i},{j}) >>> {matriz2[i][j]:02}")


##
# Maior Valor de cada linha - 4 
##
#Solicite ao usuário uma matriz 4×4 e exiba o maior elemento de cada linha.
#Tive dificuldade, fiz com a ajuda da explicação, tentei fazer com max

matriz = []
for i in range(4):
    linha= []
    for j in range(4):
        elemento=float(input("Digite um valor entre 0 e 99"))
        linha.append(elemento)
    matriz.append(linha)

print(f"{matriz}")

for linha in matriz:
    maior=0
    for elemento in linha:
        if elemento > maior:
            maior = elemento
    print(f" O maior elemento da linha: {linha} \n\t\t >>{maior}<<")

##
# Contagem de números pares - 5
##

import random

matriz = []
for i in range(4):
    linha= []
    for j in range(4):
        elemento=(random.randint(1,100))
        linha.append(elemento)
    matriz.append(linha)

par=0
impar=0

for linha in matriz:
    for elemento in linha:
        if elemento % 2 == 0:
            par = par+1
        else:
            impar = impar+1
        

print(f"{matriz}")
print(f"A quantidade de números pares é de: {par}")
print(f"A quantidade de números impares é de: {impar}")


##
# Multiplicações de linhas por números - 6
##     
# Não consegui entender nem fazer sem a explicação
import random

matriz = []
for i in range(4):
    linha= []
    for j in range(4):
        elemento=(random.randint(1,100))
        linha.append(elemento)
    matriz.append(linha)

n=float(input("Digite um número : "))

matrizmult= []
for linha in matriz:
    linhamult= []
    for elemento in linha:
        resultado = elemento*n
        linhamult.append(resultado)
    matrizmult.append(linha)

print(f"{matrizmult}")

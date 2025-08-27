import random

matriz = []
for i in range(10):
    linha= []
    for j in range(10):
        elemento=(random.randint(1,999))
        linha.append(elemento)
    matriz.append(linha)

matriz2 = []
for i in range(10):
    linha= []
    for j in range(10):
        elemento=(random.randint(1,999))
        linha.append(elemento)
    matriz2.append(linha)

soma=matriz[i][j]+matriz2[i][j]


for linha in matriz:
     print(f"{linha}")
print(f"--------------------------------------------------")
for linha in matriz2:
    print(f"{linha}")

matriz3 = []
for i in range(10):
    linha = []
    for j in range(10):
        soma = matriz[i][j] + matriz2[i][j]
        linha.append(soma)
    matriz3.append(linha)

print(f"Resultado: ")
for linha in matriz3:
    print(linha)

    soma = []
for i in range(10):
    linha = []
    for j in range(10):
        somadenumeros = matriz[i][j] + matriz2[i][j]
        linha.append(somadenumeros) 
    soma.append(linha)


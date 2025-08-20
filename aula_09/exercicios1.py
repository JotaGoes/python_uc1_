##
# Exemplo Lista
##
vetor = [10, 20, 30, 40, 50]
print(f" Dados do Vetor: {vetor} ")

print(f" Dados da 4a posicao : {vetor[3]} ")

for elemento in vetor :
    print(f" Valor do Elemento {elemento}")

for i in range(5) : 
    print(f"{i}")
    print(f"{vetor[i]}")

for i in range(5):
    print(f" O valor da {i+1}a posicao é {vetor[i]}")

indice = 1
for elemento in vetor :
    print(f" O valor do indice {indice} é {elemento}")
    indice+=1

    
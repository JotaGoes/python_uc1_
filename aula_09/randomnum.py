#import random
#n = random.randint(1, 187)
#print(f" {n} ")

#import random
#n= []
#for i in range (20):
#    n.append(random.randint(1,187))

#print(f" >> {n} << ")

#soma=sum(n)
#maior=max(n)
#menor=min(n)
#elementos=len(n)

#media=soma/elementos

#print(f" A soma dos valores é de: {soma}")
#print(f" O maior número é: {maior}")
#print(f" O menor número é: {menor}")
#print(f" Temos {elementos} elementos")
#print(f" A média é de: {media}")

##
# LISTA PAR E ÍMPAR
##

#TESTE
#import random
#vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#par = [n for n in vetor if n % 2 == 0]
#impar = [n for n in vetor if n % 2 != 0]

#print(f" A lista de números pares é de: {par}")
#print(f" A lista de números impares é de: {impar} ")

#LISTA DE NUMEROS ENTRE 1 E 20
import random
elementos=random.randint(1,150)

n=[]
for i in range(elementos):
    n.append(random.randint(1,9999))

par=[]
impar=[]

for valor in n :
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f" Os números pares são:\n\t {par} \n")
print(f" Os números impares são:\n\t {impar} \n")
print(f" A quantidade de números pares é de:\n\t {len(par)} \n")
print(f" A quantidade de números impares é de:\n\t {len(impar)} \n")
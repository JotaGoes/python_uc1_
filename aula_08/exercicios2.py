##EXERCÍCIO 2 - Aula 08
# Autor: Luis Rodrigo, vulgo Papagaio
# Data: 12/08/2025
##

## MAIN

##
# SAUDACAO 
##

def saudacao():
    print(" Ola, Mundo! ")

##
# TESTE SOMAR DOIS NUMEROS
##
def soma(n1, n2):
    soma = n1 + n2
    print(f"{soma}")

##
# SOMA DOIS NUMEROS DEFINIDOS PELO USUÁRIO
##

def somav2():
   n1 = float(input("Digite o primeiro número: "))
   n2 = float(input("Digite o segundo número: "))
   soma = n1 + n2
   print(f"A soma é: {soma}")  

##
# CHAMAR SOMA E SUBTRAÇÃO
##
def mais(a, b):
   return a + b

def menos(a, b):
   return a - b

def contas():
   resultadomais = mais(10, 5)
   resultadomenos = menos(10, 5)
   print(f"Soma: {resultadomais}")
   print(f"Subtração: {resultadomenos}")

##
# IMPRIMIR DE 1 A 10
##
def copiar():
   for i in range(1, 11):
       print(i)

##
# FATORIAL
##
def fatorial(n):
   if n == 0 or n == 1:
       return 1
   else:
       return n * fatorial(n - 1)

def nfatorial():
   num = int(input("Digite um número: "))
   print(f"O fatorial de {num} é {fatorial(num)}")

##
# MAIOR NUMERO
##
def maior_elemento(lista):
  return max(lista)

def ogrande():
    numeros = [2, 4, 6, 8, 10, 12]
    numeros = [int(num) for num in numeros]
    print("Nessa lista, o maior elemento é:", maior_elemento(numeros))

##
# STRING INVERTIDA
##

def string_invertida(frase):
   return frase[::-1]

def invertida():
   frase = input("Digite uma palavra: ")
   print(f"Frase invertida: {string_invertida(frase)}"")
         if __name__ == "__main__":
        
    #saudacao()
    #soma(20,30)
    #somav2()
    #contas() 
    #copiar()
    #nfatorial()
    #ogrande()
    invertida()
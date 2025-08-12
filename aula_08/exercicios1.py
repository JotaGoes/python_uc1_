##EXERCÍCIO 1 - Aula 08
# Autor: Luis Rodrigo, vulgo Papagaio
# Data: 12/08/2025

##
# SAUDAÇÃO
##

#def saudacao():
#    print("\n\n\t Boa noite! \n\n")

##
# SOMAR
##

#def soma(a, b):
#   return a + b

#resultado = {5+6}
#print("a soma é:", resultado)

##
# PAR OU ÍMPAR
##

#def par_ou_impar(n):
#  if n % 2 == 0:
#    return "par"
#  else:
#    return "impar" 

#print("o número 10 é:", par_ou_impar(10))
#print("o número 11 é:", par_ou_impar(11))

##
# FATORIAL
##
#def fatorial(n):
#  if n < 0:
#    return " Não é possível ser um número fatorial. "
#  elif n == 0:
#    return 1
#  else:
#     resultado = 1
#     for i in range(1, n + 1):
#       resultado *= i
#     return resultado
#
#print("O fatorial de 5 é: ", fatorial(5))

##
# MAIOR ELEMENTO
##
#def maior_elemento(lista):
#  return max(lista)
#
#numeros = [2, 4, 6, 8, 10, 12]
#print("Nessa lista, o maior elemento é:", maior_elemento(numeros))

##
# MEDIA
##

#def media(lista):
#    return sum(lista) / len(lista)
#
#numeros = [10, 30, 22, 40, 37]
#print("A media dos valores e de: ", media(numeros))

##
# PALINDROMO
##

#def eh_palindromo(string):
#  return string == string[::-1]
#
#print("A palavra EEVEE é um palíndromo? ", eh_palindromo("eevee"))
#

##
# CONTAR VOGAIS
##

#def contar_vogais(texto):
#  vogais = "aeiouAEIOU"
#  contador = 0
#  for char in texto:
#    if char in vogais:
#         contador += 1
#  return contador
#
#print("O número de vogais na palavra 'Paralelepipedo' é de: ", contar_vogais("Paralelepipedo"))

#saudacao() certo
#soma(5, 6) certo
#par_ou_impar(10,
#             11) certo
#fatorial(5) certo
#maior_elemento([2, 4, 6, 8, 10, 12]) certp
#media([10, 30, 22, 40, 37])
#eh_palindromo("eevee")
#contar_vogais("Paralelepipedo")
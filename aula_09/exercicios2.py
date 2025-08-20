#produtos = (
#    ("Arroz", 5.99),
#    ("Feijão", 7.49),
#    ("Leite", 4.89),
#    ("Óleo", 9.99),
#    ("Açúcar", 3.29)
#)

#print("LISTA DE PRODUTOS")
#for nome, preco in produtos:
#    print(f"{nome:.<20} R$ {preco:.2f}")

#produtos = (
#    ("Arroz", 5.99, 10),
#    ("Feijão", 7.49, 3),
#    ("Leite", 4.89, 5), 
#    ("Óleo", 9.99, 2),
#    ("Açúcar", 3.29, 5)
#)

#total_geral=0
#print("LISTA DE PRODUTOS")
#for nome, preco, quantidade in produtos:
#    total=preco*quantidade
#    total_geral=total_geral+total
#    print(f"{nome:.<20} R$ {preco:.2f} x {quantidade:03} = R$ {total:6.2f}")
#desconto=total_geral*0.9
#print(f"\tValor da compra: R$ {total_geral:8.2f}")
#print(f"\tDesconto : -10% ")
#print(f"\tValor final : R$  {desconto:8.2f}")

##
# DIFICULDADE NESSA, , ESTUDAR SOBRE TUPLA E SOMA DEPOIS
##

##
# Calcular valor médio da lista de 100 números aleatórios, e exibir números acima da média
##

import random
elementos=100

n=[]
for i in range(elementos):
    n.append(random.randint(1,999))


soma=sum(n)
elementos=len(n)
media=soma%elementos


acima_da_media=[]
for valor in n:
    if valor > media:
        acima_da_media.append(valor)

print(f" >> {n} <<")
print(f" A média desses elementos é de: {media}")
print(f" Os numeros maiores que a média são: {acima_da_media}")


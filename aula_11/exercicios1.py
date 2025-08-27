##
# Aula 11 - Dicionários
##

#dicionário chamado pessoa
pessoa = {
    "nome"  : "Joao",
    "idade" : 18,
    "cidade" : "Petropolis",
    "uf" : "Rj",
    "email" : "jmgoes8@gmail.com"
    }
print(pessoa)

del pessoa["uf"]
print(pessoa)

##
# ATIVIDADE
# Criar uma lista, adicionar dados de duas pessoas no formato de dicionário a lista, os dados de cada pessoa devem ficar em uma das posições da lista
##

# nome, idade, cidade, email

pessoas= []

for i in range(2):
    pessoa= {}
    pessoa["nome"]=input("Digite o seu nome: ")
    pessoa["idade"]=int(input("Digite sua idade: "))
    pessoa["cidade"]=input("Digite a cidade em que vive: ")
    pessoa["email"]=input("Digite agora o seu email: ")

    pessoas.append(pessoa)

print(f"{pessoas}")
print(pessoas[0]["nome"])

pessoas[0]["celular"]= "024 98854-5870"

print(pessoas[0])
print(pessoas[1])

##
# estruturas complexas
##

alunos = {}

#adicionar alunos
alunos[1] = {"nome": "Maria", "notas" : [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "João", "notas" : [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "Carlos", "notas" : [5.5, 6.5, 7.0]}

#calcular media
for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media,2)

print(alunos)

#usar "nome do dicionario""especificidade do dicionário".append para adicionar partes à listas vazias

##
# codigo molde do papagaio
##

alunos= {}

alunos[1]={"nome":"Zezinho", "notas":[]}
alunos[2]={"nome":"Huguinho", "notas":[]}
alunos[3]={"nome":"Luisinho", "notas":[]}

print (alunos)

alunos[1]["notas"].append(6.0)
alunos[2]["notas"].append(8.0)
alunos[3]["notas"].append(10.0)

alunos[1]["notas"].append(6.5)
alunos[2]["notas"].append(7.0)
alunos[3]["notas"].append(10.0)

alunos[1]["notas"].append(8.0)
alunos[2]["notas"].append(5.0)
alunos[3]["notas"].append(10.0)

alunos[1]["notas"].append(4.0)
alunos[2]["notas"].append(7.0)
alunos[3]["notas"].append(10.0)


print(alunos[1])

for matricula, dados_aluno in alunos.items() :
    print(f"Matricula do Aluno ..... : {matricula}")
    print(f'Nome do Aluno .......... : {dados_aluno["nome" ]}')
    #print(f"Notas do Aluno ........ : {dados_aluno["notas"]})
    print(f"Notas do Aluno ......... :")
    for nota in dados_aluno["notas"]:
        print(f"\t\tNota ... {nota}")

media=sum(dados_aluno["notas"])/len(dados_aluno["notas"])
print(f" \t\tMedia .. {media}")

dados_aluno["media"]=media

print(f'Media: {dados_aluno["media"]}')

if media >= 6:
    dados_aluno["status"]="Aprovado"
else:
    dados_aluno["status"]="Reprovado"

    print(f'Status : {dados_aluno["status"]}')
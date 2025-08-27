alunos= {}

alunos[1]={"nome" :"Zezinho", "notas":[]}
alunos[2]={"nome" :"Huguinho", "notas":[]}
alunos[3]={"nome" :"Luisinho", "notas":[]}

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

print (alunos)

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
# Observação melhorar as saidas desse desafio

from datetime import datetime

def Cadastrar_voluntario():
    nome=(input("Digite seu nome:"))
    cpf=(int(input("Digite o seu CPF:")))
    lista_voluntarios={}
    if cpf in lista_voluntarios:
        print(f"CPF {cpf} já está em uso! ")
        if not nome or cpf:
            print(f"OS campos {nome} e {cpf} não pode está vazios")
    lista_voluntarios[nome]=cpf
    print(lista_voluntarios)
def registrar_arvore():
    especie=input("Nome da especie da arvore:")
    id_arvore=int(input("Digite o indentificador da arvore de preferencia número:"))
    local=input("Local do plantio da arvore:")
    data_do_plantio=input("Data do plantio D/M/A:")
    data_formatada_plantio= datetime.strptime(data_do_plantio,"%d/%m/%Y")
    print("Data válida", data_formatada_plantio.strftime("%d/%m/%Y"))
    data_atual=datetime.today()
    quantidade_plantada=int(input("Numero de arvores plantadas:"))
    taxa_carbono=float(input("taxa de carbono:"))
    if not all([especie,id_arvore,local,data_do_plantio,quantidade_plantada,taxa_carbono,data_atual]):
        print("Todos os campos devem ser preechidos!")
    ano= data_formatada_plantio - data_atual
    print(ano)
    resultado= ano * taxa_carbono * quantidade_plantada
    print(resultado)
Cadastrar_voluntario()
registrar_arvore()

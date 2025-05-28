#Você deve criar um programa que simule um caixa eletrônico. 
# O programa deve:

class CaixaEletronico:
    def __init__(self):
        self.notas=[100,50,20,10,5,2]

# 2:Calcular quantas notas de cada tipo serão entregues.
    def sacar(self,valor):
        resultado={}
        for nota in self.notas:
            quantidade= valor // nota # quantidade de nota necessaria
            if quantidade > 0:
                resultado[nota]=quantidade
                valor=valor% nota
        if valor != 0 :
            print('Não é possivel sacar esse valor com as notas disponiveis')
            return {}

    def exibir_notas(self,notas):
        if not notas:
            return
        print("Notas entregues")
        for nota,qtd in notas.items():
         print(f"{qtd} nota(s) de R${nota}")

caixa= CaixaEletronico()
valor=int(input("Valor do saque:"))
resultado=caixa.sacar(valor)
if resultado:
    caixa.exibir_notas(resultado)




# 3:O caixa possui apenas notas de R$100, R$50, R$20, R$10, R$5 e R$2.

# 4:Exibir quantas notas de cada valor foram usadas no saque.

# 5:Se não for possível sacar o valor (ex: valor ímpar que não pode ser formado com as notas disponíveis), exiba uma mensagem de erro apropriada.
from datetime import datetime


def caixa_eletronico_inteligente():
    # O usuário deve informar um valor inteiro positivo para sacar (entre 10 e 1000 reais)
    valor_sacar=int(input("Digite de um valor que deseja sacar R$:"))
    # O caixa só possui cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.
    cedulas=[100,50,20,10,5,2]
    saque_total=valor_sacar
    dicionario={}
    #O programa deve calcular a menor quantidade de cédulas possíveis para o valor solicitado
    for cedula in cedulas:
         if valor_sacar >= cedula:
            quantidade= valor_sacar // cedula # calcula quantas vezes a cedula cabe no valor de saque
            valor_sacar -= quantidade * cedula # atualiza o valor restante
            dicionario[cedula]= quantidade # armazena a quantidade de cedula usadas
    if valor_sacar != 0:
        print(f"Não é possível sacar R$ {saque_total} com as cédulas disponíveis.")
        print(f"Valor restante impossível de sacar: R$ {valor_sacar}")
    else:
        print(f"Saque de R$ {saque_total} realizado com:")
        for cedula in cedulas:
            if cedula in dicionario:
                print(f"{dicionario[cedula]} nota(s) de R$ {cedula}")
              

        
    

funcao=caixa_eletronico_inteligente()





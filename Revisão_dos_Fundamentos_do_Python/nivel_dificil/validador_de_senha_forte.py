# DESAFIO VALIDADOR DE SENHA FORTE

# recebendo a entrada do usúario
senha=input("Digite uma senha válida:")
# verificando  se a senha tem 8 caracter
if len(senha)< 8:
    print("A Senha deve ter pelo menos 8 caracter!")
# Inicialiazando as variaveis com falso
else:
    letraMaiuscula= False
    letraminuscula= False
    digito= False
    caracter_especiais= False
    # Usando o laço de repetição para verificar cada caracter
    for caracter in senha:
        #verifica se o caracter é maiuscula
        if caracter.isupper():
            letraMaiuscula= True
        # verificar se o caracter é minusculos
        if caracter.islower():
            letraminuscula= True
        # verificar  se é um digito
        if caracter.isdigit():
            digito= True
        # verificar se tem carater especial.
        if caracter in "!@#$%&*":
            caracter_especiais = True
    if letraMaiuscula and letraminuscula and digito and caracter_especiais:
        print(F"Senha {senha} forte!")
    else:
        print(F"Senha fraca requistos")
        if not letraMaiuscula:
            print(F"Senha {senha} requer letra maiúscula!")
        if not letraminuscula:
            print(f"Senha {senha} requer letra minuscula!")
        if not digito:
            print(f"Senha {senha} requer pelo menos um digito!")
        if not caracter_especiais:
            print(F"Senha {senha} resquer pelo menos 1 caracter especial!")
    



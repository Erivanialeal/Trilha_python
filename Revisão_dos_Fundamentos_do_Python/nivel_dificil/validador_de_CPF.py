


cpf=(input("Digite o seu CPF (xxx.xxx.xxx.xx):"))
# Remover tudo que não é número
cpf_numeros="".join(char for char in cpf if char.isalnum())
#verificar se tem 11 digitos
if len(cpf_numeros) != 11:
    print(f" O CPF {cpf} deve ter 11 caracter!")
else:
    #calculo do primeiro digito verificador
    nove_digitos=cpf_numeros[:9]
    soma=0
    peso=10
    for digito in nove_digitos:
        soma += int(digito) * peso
        peso -= 1

    primeiro_digito=(soma * 10) % 11
    if primeiro_digito >= 10:
        primeiro_digito=0
    print(f"Primeiro dígito verificador calculado: {primeiro_digito}")


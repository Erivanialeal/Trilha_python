
# Desafio: Jogo de Números com Regras Especiais
# entrada número inteiro possitivo com validação
numero_entrada=(input("Digite um número inteiro positivo:"))
N=int(numero_entrada)
# Validação do número.
if N <= 0:
    print("O número precisa ser positivo.")
else:
    #contadores
    fizz=0
    buzz=0
    bazz=0
    for numero in range(1 , N + 1):
        resultado=''
        if numero % 3 ==0:
            resultado += 'Fizz'
            fizz += 1
        if numero % 5 == 0:
            resultado += "Buzz"
            buzz += 1
        if numero % 7 == 0:
            resultado += 'Bazz'
            bazz += 1
        if resultado == '':
            print(numero)
        else:
            print(resultado)
    print(f"Fizz apareceu {fizz} vezes")
    print(f"Buzz apareceu {buzz} vezes")
    print(f"Bazz apareceu {bazz} vezes")

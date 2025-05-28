#Desafio: Adivinhe o Número! (com tentativas limitadas)
# logica em linguagem natural.
import random

def adivinhe_o_numero():
    # sorteia o número secreto
    numero_aleatorio = random.randint(1, 100)
    
    tentativas = 0  # começa com zero tentativas

    while tentativas < 7:  # o jogador pode tentar até 7 vezes
        try:
            resposta = int(input(f"Tentativa {tentativas + 1}: Tente adivinhar o número de 1 a 100: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            continue  # volta para o começo do laço se digitar errado

        tentativas += 1  # conta uma tentativa

        if resposta < numero_aleatorio:
            print("Muito baixo!")
        elif resposta > numero_aleatorio:
            print("Muito alto!")
        else:
            print(f"ACERTOU! O número era {numero_aleatorio}. Você usou {tentativas} tentativas.")
            break  # sai do laço se acertar

    else:
        # só acontece se o jogador usar todas as 7 tentativas sem acertar
        print(f"Você perdeu! O número era {numero_aleatorio}.")

# chama a função para rodar o jogo
adivinhe_o_numero()

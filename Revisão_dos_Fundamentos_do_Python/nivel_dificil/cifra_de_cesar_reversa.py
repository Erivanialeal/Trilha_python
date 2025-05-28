



mensagem=input("Digite uma Mensagem:") ##recebe a entrada do usuario
mensagem_criptografada="" # uma variavel para armazenar a entrada criptografada
for letra in mensagem: # análisa cada letra em mensagem
    if letra.isalpha(): # verifica se uma string contém apenas letras
        deslocamento=3 # define o deslocamento
        if letra.isupper(): # se for maiuscula aplica o deslocamneto
            codigo = ord(letra) - deslocamento # recebe a letra em forma binaria e desloca 3 letra pra tras
            if codigo < ord('A'): # Se o novo código for menor que 'A', ajusta para o final do alfabeto
                codigo += 26 # Isso garante que a letra volte ao final do alfabeto se ultrapassar 'A'.
            nova_letra=chr(codigo) # Converte o código numérico de volta para um caractere legível
        else:
            codigo = ord(letra) - deslocamento
            if codigo < ord('a'):
                codigo += 26
            nova_letra = chr(codigo)
        mensagem_criptografada += nova_letra
    else:
         mensagem_criptografada += letra

print("Mensagem criptografada:", mensagem_criptografada)
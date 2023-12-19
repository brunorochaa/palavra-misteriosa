# Aula 47 - Palavra misteriosa
"""
Faça um jogo para o usuário advinhar uma palavra misteriosa:
    - Você vai propor uma palavra misteriosa aleatória, e, vai dar a possibilidade para o usuário digitar apenas uma letra.
    - Quando o usuário digitar a letra você irá conferir se a letra digitada está na palavra misteriosa.
        - Se a letra digitada estiver na palavra misteriosa exiba a letra.
        - Se a letra digitada não estiver na palavra misteriosa, exiba *
    - Faça a contagem de tentativas do seu usuário.
"""
import os

palavra_misteriosa = 'bruno'
letras_corretas = ''
numero_de_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').lower()
    numero_de_tentativas += 1

    if len(letra_digitada) > 1:
        print ('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_misteriosa:
        letras_corretas += letra_digitada

    palavra_formada = ''
    for letra_misteriosa in palavra_misteriosa:
        if letra_misteriosa in letras_corretas:
            palavra_formada += letra_misteriosa
        else:
            palavra_formada += '*'

    print('Palavra misteriosa:', palavra_formada)

    if palavra_formada == palavra_misteriosa:
        os.system('cls')
        print(f'VOCÊ GANHOU! EM {numero_de_tentativas} TENTATIVAS, PARABÉNS!')
        break
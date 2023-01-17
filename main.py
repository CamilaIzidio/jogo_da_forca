###############################################################################
####               *********** JOGO DA FORCA ***********                   ####
###  O principal ponto treinado foi em relação à lógica de programação,     ###
###  estruturas de repetição, uso das estruturas de dados de conjunto e     ###
###  dicionário, ler entrada de dados do usuário, leitura de arquivo        ###
###  (conjunto das palavras, e a utilização da biblioteca random do Python  ###
###  para escolher a palavra dentre a lista.                                ###
###############################################################################

import random
import string
from palavras import palavras
from visual import dicionario_visual_letras

def escolher_palavra(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)
    return palavra.upper()

def imprime_mensagem_vencedor(palavra):
    print("A palavra era {}".format(palavra))
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print("A palavra era {}".format(palavra))
    print("Que pena, você perdeu!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def forca():
    palavra = escolher_palavra(palavras)
    letras_da_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set()
    vidas = 7

    while len(letras_da_palavra) > 0 and vidas > 0:
        print('Você tem {} vidas restantes e você já utilizou essas letras: {}'.format(vidas,' '.join(letras_utilizadas)))
        lista_letras = [letra if letra in letras_utilizadas else '-' for letra in palavra]
        print(dicionario_visual_letras[vidas])
        print('Palavra: ', ''.join(lista_letras))

        letra_da_rodada = input('Escolha uma letra: ').upper()
        if letra_da_rodada in alfabeto - letras_utilizadas:
            letras_utilizadas.add(letra_da_rodada)
            if letra_da_rodada in letras_da_palavra:
                letras_da_palavra.remove(letra_da_rodada)
                print('')
            else:
                vidas -= 1
                print('\nEssa letra não está na palavra.')
        elif letra_da_rodada in letras_utilizadas:
            print('Você já escolheu essa letra anteriormente. Tente novamente.')
        else:
            print('Caracter inválido. Tente novamente.')
    if vidas == 0:
        print(dicionario_visual_letras[vidas])
        imprime_mensagem_perdedor(palavra)
    else:
        imprime_mensagem_vencedor(palavra)

forca()
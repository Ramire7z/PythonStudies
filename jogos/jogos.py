import random
import sys

import adivinhacao
import forca


def escolha_o_jogo():
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo você deseja jogar? "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação")
        adivinhacao.jogar()

    resposta = str(input("\nAperte qualquer tecla para jogar novamente! Ou feche o jogo e seja feliz."))
    if resposta == "s" or "sim":
        print("\nReiniciando...")
        escolha_o_jogo()


# Faz com que forca.py execute o código enquanto, simultaneamente, a função jogar() pode ser chamada e executada em
# jogos.py sem que o código seja executado instantaneamente após a importação.
if __name__ == "__main__":
    escolha_o_jogo()

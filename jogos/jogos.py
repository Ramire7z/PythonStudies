import random
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

if __name__ == "__main__":
    escolha_o_jogo()
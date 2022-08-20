print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    try:
        chute = int(chute_str)
    except:
        print("Você precisa digitar um número entre 1 e 100, não utilize letras!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    if acertou:
        print("Parabéns! Você acertou.")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")

    rodada = rodada + 1

print("Fim do jogo")

import random

numero_secreto = random.randint(1, 100)

tentativas = 0
limite = 7
acertou = False

print("Tente adivinhar o número entre 1 e 100!")
print(f"Você tem {limite} tentativas.\n")


while tentativas < limite:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        acertou = True
        break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")

    print(f"Tentativas restantes: {limite - tentativas}\n")


if not acertou:
    print(f"Você perdeu! O número era {numero_secreto}.")

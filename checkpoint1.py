import random

# 1. Computador escolhe um número
numero_secreto = random.randint(1, 100)

tentativas = 0
limite = 7
acertou = False

print("🎯 Tente adivinhar o número entre 1 e 100!")
print(f"Você tem {limite} tentativas.\n")

while tentativas < limite:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

import random

tentativa = 0
palpite = 0
num = random.randint(1, 100)

Print("JOGO DE ADIVINHAÇÃO")
print("Tente adivinhar o número secreto entre 1 e 100 para vencer!")

while True:
    if tentativa == 7:
        print(f"Você perdeu. O número máximo de tentativas foi atingido. O número secreto era {num}.")
        break

    palpite = int(input("Digite um número: "))
    
    if palpite == num:
        print(f"Você venceu! O número secreto era {num}.")
        break
    elif palpite > num:
        print("O número secreto é menor.")
    else:
        print("O número secreto é maior.")

    tentativa += 1

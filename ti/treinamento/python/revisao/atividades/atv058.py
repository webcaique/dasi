from random import randint
from time import sleep


print("Sou seu conputador", end="")
for i in range(0,3):
    print(".",end="")
    sleep(1)
boot = randint(0,10)
print(" Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
player = cont = 0
while player != boot:
    player = int(input("Qual é seu palpite? "))
    if player < boot:
        print("Mais... Tente mais uma vez.")
    elif player > boot:
        print("Menos... Tente mais uma vez.")
    cont += 1

print(f"Acertou com {cont} tentativas. Parabéns!!!")

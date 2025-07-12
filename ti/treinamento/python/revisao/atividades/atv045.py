from random import randint
from time import sleep


print("""Suas opções:
[ 1 ] PEDRA 
[ 2 ] PAPEL
[ 3 ] TESOURA""")
player = int(input("Qual é sua jogada? "))
boot = randint(1,3)

if (player == 1 and boot == 2) or (player == 2 and boot == 3) or (player == 3 and boot == 1):
    res = "PERDEU"
elif (player == 2 and boot == 1) or (player == 3 and boot == 2) or (player == 1 and boot == 3):
    res = "VENCEU"
elif player == boot:
    res = "EMPATOU"

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

if player == 1:
    player = "PEDRA"
elif player == 2:
    player = "PAPEL"
elif player == 3:
    player = "TESOURA"

if boot == 1:
    boot = "PEDRA"
elif boot == 2:
    boot = "PAPEL"
elif boot == 3:
    boot = "TESOURA"

print("-="*10)
print(f"""Computador jogou {boot}
Jogador jogou {player}""")
print("-="*10)
print(f"JOGADOR {res}")
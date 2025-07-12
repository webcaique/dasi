from random import randint
from time import sleep


print("=-"*25)
print("Vou pensar em um número entre 0 e 5, tente adivinhar!")
print("=-"*25)
num = int(input("Em que número eu pensei? "))
print("Processando", end="")
sleep(1)
print(".",end="")
sleep(1)
print(".", end="")
sleep(1)
print(".")
sleep(1)
sorte = randint(0,5)
print(f"{"Ganheu" if num == sorte else "Perdeu"}! Pensei no número {sorte}{"." if num == sorte else f" e não no {num}."}")


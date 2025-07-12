from random import randint


print("-="*20)
print(f"{'JOGO DE PAR E ÍMPAR':^40}")
print("-="*20)
cont = 0
while True:
    player_num = int(input("Diga um valor: "))
    player = str(input("Par ou Ímpar: [P/I] ")).strip().upper()[0]
    while player not in "PI":
        print("~~" * 20)
        print("ENTRADA INVÁLIDA! Tente novamente.")
        print("~~" * 20)
        player = str(input("Par ou Ímpar: [P/I] ")).strip().upper()[0]

    boot_num = randint(1, 10)

    soma = player_num + boot_num
    print("--" * 20)
    print(f"Vocẽ jogou {player_num} e o computador {boot_num}. Total de {soma}", end=" ")
    if soma % 2 == 0:
        print("DEU PAR!")
        print("--" * 20)
        if player == "P":
            print("VOCẼ VENCEU!")
            cont += 1
        else:
            print("VOCẼ PERDEU!")
            break
    else:
        print("DEU ÍMPAR!")
        print("--" * 20)

        if player == "I":
            print("VOCẼ VENCEU!")
            cont += 1
        else:
            print("VOCẼ PERDEU!")
            break
    print("--" * 20)
    print("VAMOS JOGAR NOVAMENTE...")
    print("--" * 20)
print("-="*20)
print(f"GAME OVER! Você venceu {cont} vezes.")

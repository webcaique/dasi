continuar = "S"
cont = num = maior = menor = soma = 0
while continuar != "N":
    if continuar not in "SN":
        print("Dado inválido. Digite novamente")
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    else:
        num = float(input("Digite um número: "))
        soma += num
        if cont == 0:
            menor = num
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
        cont += 1
        continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
print(f"Você digitou {cont} números e a média foi {( soma / cont ):.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")

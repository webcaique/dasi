cont18 = conH = contM20 = 0

while True:
    print("--" * 20)
    print(f"{'CADASTRE UMA PESSOA':^40}")
    print("--" * 20)

    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    while sexo not in "MF":
        print("~~" * 20)
        print("ENTRADA INVÁLIDA! Tente novamente!")
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    print("--" * 20)

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    while continuar not in "SN":
        print("~~" * 20)
        print("ENTRADA INVÁLIDA! Tente novamente!")
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if idade > 18:
        cont18 += 1

    if sexo == "M":
        conH += 1

    if sexo == "F" and idade < 20:
        contM20 += 1

    if continuar == "N":
        break
print("--" * 20)
print(f"Total de pessoas com mais de 18 anos: {cont18}.")
print(f"Ao temos {conH} homens cadastrados.")
print(f"E temos {contM20} mulheres com menos de 20 anos.")

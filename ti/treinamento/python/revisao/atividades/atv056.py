"""
Média de idade
O homem mais velho, idade e nome
Qtde de mulheres com menos de 20 anos
"""
totalIdade = 0
homemVelhoIdade = 0
homemVelho = ""
contW20 = 0
for i in range(1,5):
    print(f"{f' {i}ª Pessoa ':-^21} ")
    name = " ".join(str(input("Nome: ")).strip().title().split())
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    totalIdade += idade
    if sexo == "M":
        if homemVelhoIdade < idade:
            homemVelhoIdade = idade
            homemVelho = name
    elif (sexo == "F") and (idade < 20):
        contW20 += 1

print(f"""A média de idade do grupo é de {(totalIdade/4):.2f} anos.
O homem mais velho tem {homemVelhoIdade} e se chama {homemVelho}.
Ao todo são {contW20} mulheres com menos de 20 anos.""")
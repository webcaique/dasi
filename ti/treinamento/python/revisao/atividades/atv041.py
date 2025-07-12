from datetime import date

nasc = int(input("Ano de nascimento do atetla: "))
atual = date.today().year
idade = atual - nasc
print(f"O atleta tem {idade} anos.")
print(f"Classificação: ", end="")
if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JÚNIOR")
elif idade <= 25:
    print("SÊNIOR")
else:
    print("MASTER")
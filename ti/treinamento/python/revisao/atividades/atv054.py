from datetime import date

today = date.today().year
contMenor = 0
contMaior = 0
for i in range(1,8):
    year = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    if (today - year) >= 18:
        contMaior += 1
    else:
        contMenor += 1
print(f"Ao todo tivemos {contMaior} pessoas maiores de idade.\nE tivemos {contMenor} pessoas menores de idade.")


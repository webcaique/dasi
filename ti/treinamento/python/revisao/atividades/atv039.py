from datetime import date

nasc = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}.")
if idade > 18:
    print(f"Você deveria ter se alistado há {idade-18} anos.")
    print(f"Seu alistamento foi em {nasc+18}")
elif idade < 18:
    print(f"Ainda faltam {18-idade} anos para o alistamento")
    print(f"Seu alistamento será em {nasc+18}")
else:
    print("Você tem que se alistar IMEDIATAMENTE!")

print("="*25)
print(f"{"TERMOS DE UMA PA":^25}")
print("="*25)
termo1 = termon = float(input("Primeiro termo: "))
razao = float(input("Razão: "))
adicional = 10
while (termo1 + (adicional * razao)) > termon:
    print(f"{termon}", end=" -> ")
    termon += razao
    if (termo1 + (adicional * razao)) == termon:
        print("Pausa")
        adicional += int(input("Quantos termos você quer mostrar a mais? "))
print("Fim!")
print(f"Progressão finalizada com {adicional} termos mostrados.")
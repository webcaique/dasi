print("="*25)
print(f"{"10 TERMOS DE UMA PA":^25}")
print("="*25)
termo1 = termon = float(input("Primeiro termo: "))
razao = float(input("Razão: "))
while (termo1 + 9 * razao) >= termon:
    print(f"{termon}", end=" -> ")
    termon += razao
print("Fim!")

print("="*25)
print(f"{"10 TERMOS DE UMA PA":^25}")
print("="*25)

first = float(input("Primeiro termo: "))
razao = float(input("Razão: "))
termos = first
for i in range(1,11,1):
    print(f"{termos} ➡", end= " ")
    termos += razao
print("Acabou")
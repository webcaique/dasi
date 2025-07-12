num = int(input("Digite um número para ver sua taboada: "))
print(f"{f' Taboada {num} ':=^14}")
for i in range(1,11):
    print(f"{num} x {i:>2} = {(i*num)}")
print("="*14)
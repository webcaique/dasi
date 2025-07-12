num = int(input("Digite um número para o cálculo do fatorial: "))
fatorial = 1
print(f"Fatorial de {num}! = {fatorial if num == 0 else ""}", end="")
for i in range(num, 0, -1):
    fatorial *= i
    print(f"{i}" + (" x " if i != 1 else f" = {fatorial}"), end="")
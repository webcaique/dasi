num = int(input("Digite um número para cálcular o fatorial: "))
fatorial = num
print(f"O fatorial de {num}! = ", end=("" if num != 0 else "1"))
while num != 0:
    print(f"{num} ", end=("x " if num != 1 else f"= {fatorial}"))
    fatorial *= (num - 1)
    num -= 1
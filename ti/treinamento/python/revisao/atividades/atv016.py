from math import floor, trunc

num = float(input("Digite um número: "))
print(f"O valor digita foi {num} e sua porção inteira é {int(num)}")
print(f"O valor digita foi {num} e sua porção inteira é {floor(num)}")
print(f"O valor digita foi {num} e sua porção inteira é {trunc(num)}")
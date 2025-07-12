num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))

maior = num1
menor = num1
if maior < num2:
    maior = num2
else:
    menor = num2

if maior < num3:
    maior = num3

if menor > num3:
    menor = num3

print(f"O maior valor digitado foi {maior}.")
print(f"O menor valor digitado foi {menor}.")

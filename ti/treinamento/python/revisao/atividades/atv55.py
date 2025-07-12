maior = 0
menor = 0
for i in range(1,6):
    weight = float(input(f"Peso da {i}ª pessoa: "))
    if maior < weight:
        maior = weight
    if i ==1:
        menor = weight
    if menor > weight:
        menor = weight
print(f"O maior peso lido foi de {maior:.2f}Kg")
print(f"O menor peso lido foi de {menor:.2f}Kg")

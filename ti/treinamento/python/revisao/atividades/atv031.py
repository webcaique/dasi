dist = float(input("Qual é a distância de sua viagem?(KM) "))
print(f"Você está preste a começar uma viagem de {dist:.2f}Km")
"""
if(dist <= 200):
    res = dist*0.5
else:
    res = dist*0.45
"""

res = dist *(0.5 if dist <=200 else 0.45)
print(f"E o preço de sua passagem será de R${res:.2f}")
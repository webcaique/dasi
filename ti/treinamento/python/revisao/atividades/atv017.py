from math import pow, sqrt, hypot

catO = float(input("Comprimento do cateto oposto: "))
catA = float(input("Comprimento do cateto adjacente: "))

#hipo = sqrt(pow(catA, 2) + pow(catO, 2))
hipo = hypot(catA, catO)

print(f"A hipotenusa vai medir {hipo:.2f}")
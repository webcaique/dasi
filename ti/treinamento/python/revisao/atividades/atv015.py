km = float(input("Quantos quilometros que se usou o carro: "))
days = int(input("Qauntos dias o carro foi alugado: "))
# 60/dia e 0,15/km
price = (km*0.15) + (days*60)
print(f"O total a pagar é R$ {price:.2f}")
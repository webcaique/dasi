weight = float(input("Qual é o seu peso? (KG) "))
heigth = float(input("Qual é a sua altura? (m)"))
imc = weight / (heigth * heigth)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
    print("Você está em ABAIXO DO PESO normal!")
elif imc < 25:
    print("PARABÉNS, você está na faixa de PESO IDEAL!")
elif imc < 30:
    print("Você está em SOBREPESO!")
elif imc < 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")

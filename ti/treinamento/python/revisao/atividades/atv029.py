speed = float(input("Qual é a velocidade atual do carro? (km/h) "))
if(speed > 80):
    print("Multado! Você exedeu o limite de 80km/h.")
    print(f"Você deve paragar uma multa de R${(speed-80)*7:.2f}!")
print("Tenha um bom dia! Dirija com segurança!")
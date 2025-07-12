import requests;
link = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

req = requests.get(link)

cash = float(input("Quanto dinheiro você tem na carteira? R$ "))
dol = float(req.json()["USDBRL"]["high"])
print(f"Com R$ {cash:.2f} você pode comprar U$D {(cash/dol):.2f}")

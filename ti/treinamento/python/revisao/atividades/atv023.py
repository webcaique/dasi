num = int(input("Digite um número: "))
uni = int(num%10)
dez = int((num%100 - uni)/10)
cent = int((num%1000 - uni - dez)/100)
milhar = int((num%100000 - uni - dez - cent)/1000)

"""
uni = int(num%10)
dez = int(num%100//10)
cent = int(num%1000//100)
milhar = int(num//1000)
"""

print(f"Número digitado é {num}")
print(f"UNIDADE: {uni}")
print(f"DEZENA: {dez}")
print(f"CENTENA: {cent}")
print(f"MILHAR: {milhar}")


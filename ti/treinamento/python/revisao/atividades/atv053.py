phrase = "".join(str(input("Digite uma frase: ")).upper().strip().split())
palindromo = ""
for i in range(len(phrase)-1, -1, -1):
    palindromo = palindromo+phrase[i]
res = "NÃO " if palindromo != phrase else ""
print(f"O inverso de {phrase} é {palindromo}")
print(f"A frase digitada {res}é um palíndromo!")

"""
STYLE => 0 (NONE), 1(BOLD), 4(UNDERLINE, 7(NEGATIVE)
TEXTCOLOR => 30(BRANCO), 31(VERMELHOR), 32(VERDE), 33(AMARELO), 34(AZUL), 35(ROXO), 36(CIANO), 37(CINZA)
BACKCOLOR => 40(BRANCO), 41(VERMELHOR), 42(VERDE), 43(AMARELO), 44(AZUL), 45(ROXO), 46(CIANO), 47(CINZA)
"""
num = int(input("Digite um número inteiro: "))
cont = 0
for i in range(1,num+1):
    color = "\033[0:31m"
    if (num % i) == 0:
        cont += 1
        color = "\033[0:33m"
    text = f"{color}{i}\033[m"
    print(text, end=" ")

print(f"\nO número {num} foi divisível {cont} vezes")
res = "NÃO " if cont > 2 else ""
print(f"Portanto, ele {res}É PRIMO")
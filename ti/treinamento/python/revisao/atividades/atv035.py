from math import fabs


l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))
res = "NÃO "

if (fabs(l2 - l3) < l1) and (l1 < (l2 + l3)):
    if (fabs(l1 - l3) < l2) and (l2 < (l1 + l3)):
        if (fabs(l1 - l2) < l3) and (l3 < (l1 + l3)):
            res = ""

print(f"Os segmentos acima {res}PODEM FORMAR Um triângulo")
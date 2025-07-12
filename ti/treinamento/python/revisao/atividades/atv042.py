from math import fabs


print("-="*40)
print(f"{"ANALISANDO A CONDIÇÃO DE EXISTÊNCIA PARA TRIÂNGULOS":^80}")
print("-="*40)
l1 = int(input("Primeiro segmento: "))
l2 = int(input("Segundo segmento: "))
l3 = int(input("Terceiro segmento: "))

if ((fabs(l2 - l3) < l1) and (l1 < l2 + l3)) and ((fabs(l1 - l3) < l2) and (l2 < (l1 + l3))) and ((fabs(l1 - l2) < l3) and (l3 < (l1 + l2))):
    if (l1 == l2) and (l1 == l3):
        print("Os segmentos PODEM FORMAR um triângulo EQUILÁTERO!")
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print("Os segmentos PODEM FORMAR um triângulo ISÓCELES!")
    else:
        print("Os segmentos PODEM FORMAR um triângulo ESCALENO!")
else:
    print("Os segmentos NÃO PODEM FORMAR um triângulo!")
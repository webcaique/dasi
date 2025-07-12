n = cont = soma = 0
while n != 999:
    """
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        soma += n
        cont += 1
    """
    soma += n
    n = int(input("Digite um número [999 para parar]: "))
    cont += 1 if n != 999 else 0
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")

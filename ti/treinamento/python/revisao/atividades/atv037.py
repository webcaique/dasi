num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para a conversão: ")
print("[ 1 ] converte para BINÁRIO")
print("[ 2 ] converte para OCTAL")
print("[ 3 ] converte para HEXADECIMAL")
conv = int(input(f"Sua opção: "))
if conv == 1:
    num_conv = bin(num)[2:]
    conv = "BINÁRIO"
elif conv == 2:
    num_conv = oct(num)[2:]
    conv = "OCTAL"
elif conv == 3:
    num_conv = hex(num)[2:]
    conv = "HEXADECIMAL"

print(f"{num} convertido para {conv} é igual a: {num_conv}")
num1 = (input("Digite um número:"))
while(not num1.isnumeric()):
    num1 = (input("Digite um número:"))

num2 = (input("Digite outro número:"))
while(not num2.isnumeric()):
    num2 = (input("Digite outro número"))

print(f'A soma entre {num1} e {num2} é {int(num1)+int(num2)}')

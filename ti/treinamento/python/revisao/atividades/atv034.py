salario = float(input("Qual o salário será atualizado? R$"))
if salario > 1250:
    res = salario * 1.1
else:
    res = salario * 1.15
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${res:.2f} agora.")

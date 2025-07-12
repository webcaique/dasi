house_value = float(input("Digite o valor da casa: R$ "))
salary = float(input("Qual o seu salário? R$"))
years = int(input("Por quantos anos você pretende em pagar? "))
prestacao = (house_value / (years * 12))
print(f"Para pagar uma casa de R${house_value:.2f} em {years} anos a prestação será de R${prestacao:.2f}")
if (salary * 0.3) < prestacao:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO APROVADO!")
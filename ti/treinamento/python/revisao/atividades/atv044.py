price = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
payment = int(input("Qual é a opção? "))
p_atual = price
if payment == 1:
    p_atual *= 0.9
elif payment == 2:
    p_atual *= 0.95
elif payment == 3:
    print(f"Sua compra será parcela em 2x de R${(price/2):.2f}.")
elif payment == 4:
    part = int(input("Quantas parcelas? "))
    p_atual *= 1.2
    print(f"Sua compra será parcela em {part}x de R${(p_atual/part):.2f} COM JUROS.")
print(f"Sua compra de R${price:.2f} vai custar R${p_atual:.2f} no final")

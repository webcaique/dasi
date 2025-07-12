print("-"*30)
print(f"{"LOJA SUPER BARATÃO":^30}")
produto1000 = compra = maisBaratoPreco = maisBaratoNome = 0
while True:
    print("-" * 30)

    nomeProduto = " ".join(str(input("Nome do Produto: ")).strip().title().split())
    preco = float(input("Preço: R$"))

    print("-" * 30)

    if maisBaratoPreco == 0 or maisBaratoPreco > preco:
        maisBaratoPreco = preco
        maisBaratoNome = nomeProduto

    if preco > 1000:
        produto1000 += 1

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    while continuar not in "SN":
        print("~" * 30)
        print("ENTRADA INVÁLIDA! Tente novamente.")
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        print("~" * 30)

    compra += preco


    if continuar == "N":
        print("-" * 30)
        print(f"{' FIM DO PROGRAMA ':-^30}")
        break

print(f"O total da compra foi R${compra:.2f}")
print(f"Temos {produto1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {maisBaratoNome} que custa R${maisBaratoPreco:.2f}")
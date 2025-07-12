from time import sleep


opcao = 4
res = ""
while opcao != 5:
    if str(opcao) not in "12345":
        print("Opção inválida. Tende novamente: ")
        sleep(2)
    else:
        if opcao == 4:
            print("Informe os números novamente: \n" if res else "", end="")
            num1 = float(input("Primeiro valor: "))
            num2 = float(input("Segundo valor: "))
            res = True
        if opcao == 1:
            print(f"A soma entre {num1} + {num2} é {num1 + num2}")
            sleep(3)
        if opcao == 2:
            print(f"A multiplicação entre {num1} e {num2} é {num1 * num2}")
            sleep(3)
        if opcao == 3:
            if num1 < num2:
                print(f"Entre {num1} e {num2} o maior é {num2}")
            elif num1 > num2:
                print(f"Entre {num1} e {num2} o maior é {num1}")
            else:
                print("Ambos tem o mesmo valor")
            sleep(3)
    print(f"""{"-="*20}  
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa""")
    opcao = int(input(">>>>> Qual a sua opção? "))
    print("-="*20)

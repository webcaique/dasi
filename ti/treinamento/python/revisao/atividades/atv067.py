while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*37)
    if n < 0:
        break
    for i in range(1,11):
        print(f"{n} x {i:>2} = {n * i}")
    print("-" * 37)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")

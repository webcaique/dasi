print("-"*20)
print("SEQUÊNCIA DE FIBONACCI")
print("-"*20)
anterior = 0
atual = 1
n = int(input("Quantos termos você quer mostrar? "))
i = 0
while i < (n/2):
    print(f"{anterior} -> {atual} ->", end=" ")
    anterior += atual
    atual += anterior
    i += 1
print("Fim!")
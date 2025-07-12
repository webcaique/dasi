nota1 = float(input("Digita a primeira nota: "))
nota2 = float(input("Digita a segunda nota: "))
media = (nota1 + nota2)/2
print(f"Tirando {nota1} e {nota2}, a média do aluno é {media}")
print("O aluno está ", end="")
if media < 5:
    print("REPROVADO!")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO!")
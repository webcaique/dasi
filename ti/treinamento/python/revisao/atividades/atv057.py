sexo = str(input("Informe seu sexo: [M/F] ")).upper().strip()[0]
while sexo not in "MF":
    print("Dados inválidos. Por favor, informe seu sexo: ", end="")
    sexo = str(input()).upper().strip()[0]

print(f"Sexo {sexo} registrado com sucesso!")
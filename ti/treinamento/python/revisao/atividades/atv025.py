name = " ".join(
    str(input("Qual é o seu nome completo? ")).strip().title().split()
)

print(f"Seu nome tem Silva? {"Sim!" if "Silva" in name else "Não!"}")
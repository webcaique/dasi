name = str(input("Qual é seu nome completo? ")).title().strip().split()
print(f"Muito prazer em te conhecer!\nSeu primeiro nome é {name[0]}.\nSeu último nome é {name[len(name)-1]}")
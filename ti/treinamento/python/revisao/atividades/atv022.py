from time import sleep


name = str(input("Digite seu nome completo: ")).title().strip()
print("Analisando seu nome",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".")
sleep(1)

print(f"Seu nome em maiúscula é {name.lower()}.")
print(f"Seu nome em minúscula e {name.upper()}.")
print(f"Seu nome tem {len(name) - name.count(' ')} letras.")
print(f"Seu primeiro nome é {name.split()[0]}, e tem {len(name.split()[0])} letras.")
heigth = float(input("Digite a altura da parede (em metros): "))
width = float(input("Digite a largura da parede (em metros): "))
square = heigth*width

print(f"A parede de dimensão {width:.2f}mX{heigth:.2f}m tem {square:.2f}m²")
print(f"Se a cada metro quadrado precisa de 2 litros de tinta, a parede precisará {(square/2):.2f}l para ser pintada.")


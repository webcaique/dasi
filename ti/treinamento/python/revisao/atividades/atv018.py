from math import sin, cos, tan, radians

degree = (float(input("Digite um ângulo: ")))
rads = radians(degree)
print(f"O ângulo de {degree:.2f}° tem o SENO de {sin(rads):.2f}")
print(f"O ângulo de {degree:.2f}° tem o COSSENO de {cos(rads):.2f}")
print(f"O ângulo de {degree:.2f}° tem o TANGENTE de {tan(rads):.2f}")

phrase = " ".join(str(input("Digite uma frase: ")).lower().strip().split())
print(f"A letra A apareceu {phrase.count("a")} vezes na frase.")
print(f"A sua primeira ocorrência aconteceu na posição {phrase.find("a")+1}.")
print(f"A última letra A apareceu na posição {phrase.rfind("a")+1}.")

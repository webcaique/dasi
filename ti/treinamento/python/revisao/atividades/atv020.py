from random import shuffle


lista = list()

while len(lista)<4:
    lista.append(
        " ".join(
            str(
                input(f"Digite a {len(lista)+1}º pessoa: ")
            ).title().strip().split()
        )
    )

    teste = lista[len(lista)-1]
    while(teste.isnumeric() or len(teste) == 0):
        lista[len(lista)-1] = (
            " ".join(
                str(
                    input(
                        f"Digite a {len(lista)}º pessoa: "
                    )
                ).title().strip().split()
            )
        )
        teste = lista[len(lista)-1]
print("A sequência selecionado foi: ")
shuffle(lista)
print(lista)

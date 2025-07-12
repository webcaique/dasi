from datetime import date


ano = int(input("Que ano quer analisar? Digite 0 para o ano atual: "))
if(ano == 0):
    ano = date.today().year
if ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} NÃO é BISSEXTO")


"""
ano = str(int(input("Que ano quer analisar? Digite 0 para o ano atual: ")))
if int(ano) == 0:
    ano = str(date.today().year)
verif = (ano[len(ano)-2:])
res = False
if int(verif) %4 == 0 :
    if verif == "00" :
        if int(ano) % 400 == 0:
            res = True
    else:
        res = True

print(f"O ano {ano}{" NÃO " if not res else " "}é BISSEXTO!")
"""
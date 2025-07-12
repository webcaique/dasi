num = int(input("Digite um número: "))
# 6 x 10 = 60 -> 11
print(F"""
{'TABUADA':=^13}
{num} x  1 = {(num*1):>2}
{num} x  2 = {(num*2):>2}
{num} x  3 = {(num*3):>2}
{num} x  4 = {(num*4):>2}
{num} x  5 = {(num*5):>2}
{num} x  6 = {(num*6):>2}
{num} x  7 = {(num*7):>2}
{num} x  8 = {(num*8):>2}
{num} x  9 = {(num*9):>2}
{num} x 10 = {(num*10):>2}
""")
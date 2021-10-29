import re

a=input("Введите первое слово:")
if not re.match("^[a-zA-Za-яА-ЯёЁ]*$", a):
    print("Error! Только буквы!")
    quit()

b = input("Введите второе слово:")
if not re.match("^[a-zA-Za-яА-ЯёЁ]*$", b):
    print("Error! Только буквы!")
    quit()

def tanimoto(a,b):
    c=[v for v in a if v in b]
    return float(len(c))/(len(a)+len(b)-len(c))
print(tanimoto(a,b))


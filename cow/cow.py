import numpy as np
import re

filename=('fib.cow','hello.cow')
file = open(filename[1], 'r') #filiname[0] для чисел Фибоначчи, filename[1] для Hello, World!
res = file.read()
rr = re.sub(r'\n', r' ', res)
rr = rr.split(' ')
stack = []
dic = {}
ind = 0
result = np.zeros(1000)
for item in rr:
    if item == 'MOO':
        stack.append(ind)
    if item == 'moo':
        dic[ind] = stack[len(stack) - 1]
        dic[stack.pop()] = ind
    ind += 1
index = 0
i = 0

while (i != len(rr)):
    if rr[i] == 'MoO':
        result[index] += 1
    if rr[i] == 'MOo':
        result[index] -= 1
    if rr[i] == 'moO':
        index += 1
    if rr[i] == 'mOo':
        index -= 1
    if rr[i] == 'OOM':
        print(chr(int(result[index])))
    if rr[i] == 'Moo':
        if rr[index] != 0:
            print(chr(int(result[index])))
    if rr[i] == 'OOO':
        rr[index] = 0
    if rr[i] == 'moo':
        i = dic[i] - 1
    if rr[i] == 'MOO':
        if result[index] == 0:
            i = dic[i]
    if rr[i] == '':
        pass
    else:
        i += 1
        continue
    i += 1

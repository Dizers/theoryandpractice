file = open("lorem.txt").read()
res = {i: file.count(i) for i in set(file)}
print(str(res))
walls = [2,5,1,3,1,2,1,6]
lmax = 0
rmax = 0
total = 0

for i in range(0, len(walls)):
    if walls[i] > walls[rmax]:
        rmax = i

for i in range(0, len(walls)):
    if walls[i] > walls[lmax] and walls[i] <= walls[rmax] and i < rmax:
        lmax = i

if rmax < lmax:
    lmax, rmax = rmax, lmax

maxheight = walls[rmax] if walls[rmax] < walls[lmax] else walls[lmax]

l = walls[lmax + 1:rmax]

for i in l:
    total += (maxheight - i)

print(total)
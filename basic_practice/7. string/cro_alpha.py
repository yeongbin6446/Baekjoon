a = input()

cro = {'c=' : 0, 'c-' : 0, 'dz=' : 0, 'd-' : 0, 'lj' : 0, 'nj' : 0, 's=' : 0, 'z=' : 0}

for x in cro:
    if x in a:
        cro[x] = a.count(x)
    else:
        continue

cnt = 0
if cro['dz='] > 0:
    for i in range(cro['dz=']):
        cro['z='] -= 1
        cnt +=1

for x in cro:
    cnt = cnt + cro[x]

print(len(a)-cnt)




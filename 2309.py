hl = []
for i in range(9):
    h = int(input())
    hl.append(h)

arr = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    for j in range(9):
        if i != j and i < j:
            temp = hl.copy()
            temp.remove(hl[i])
            temp.remove(hl[j])
            arr[i][j] = sum(temp)

for i in range(9):
    for j in range(9):
        if arr[i][j] == 100:
            r1 = hl[i]
            r2 = hl[j]
            break

hl.remove(r1)
hl.remove(r2)
hl.sort()

for i in hl:
    print(i)
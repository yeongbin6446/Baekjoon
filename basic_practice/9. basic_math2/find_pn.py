from sys import stdin

N = int(stdin.readline())
x = list(map(int,stdin.readline().split()))

cnt = 0
flag = True
for i in range(N):
    if x[i] == 1:
        continue
    if x[i] == 2:
        flag = True
    for j in range(2, x[i]):
        if x[i] % j == 0:
            flag = False
            break
        flag = True

    if flag:
        cnt += 1

print(cnt)




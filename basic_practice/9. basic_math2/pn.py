M = int(input())
N = int(input())

prime = []
for i in range(M,N+1):
    flag = True
    if i == 1:
        continue
    elif i == 2:
        flag = True
    else:
        for j in range(2, i):
            if i % j == 0: #소수가 아님
                flag = False
                break
    if flag:
        prime.append(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))


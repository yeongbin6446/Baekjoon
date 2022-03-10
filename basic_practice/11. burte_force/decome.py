N = int(input())

ans = []
for i in range(1,N+1):
    m = str(i)
    d = i
    for j in range(len(m)):
        d += int(m[j])
    if d == N:
        ans.append(i)

if ans:
    print(min(ans))
else:
    print('0')


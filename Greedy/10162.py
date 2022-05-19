N = int(input())

time = [300, 60, 10]
cnt = []
for t in time:
    if N // t >= 0:
       cnt.append(N//t)
       N = N % t

if N != 0:
    print(-1)
else:
    print(*cnt)
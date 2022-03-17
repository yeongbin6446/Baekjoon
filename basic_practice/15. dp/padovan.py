def P(n):
    if n <= 2:
        return 1
    p = [0] * (n+1)
    p[0] = 1
    p[1] = 1
    p[2] = 1
    for i in range(3, n+1):
        p[i] = p[i-3] + p[i-2]

    return p[i-1]

for i in range(int(input())):
    n = int(input())
    print(P(n))
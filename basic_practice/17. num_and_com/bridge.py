def fac(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
N = int(input())
for i in range(N):
    left, right = map(int, input().split())
    ans = fac(right) // (fac(left) * fac(right - left))
    print(ans)

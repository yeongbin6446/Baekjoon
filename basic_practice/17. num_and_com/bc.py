def fac(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
N, K = map(int, input().split())
ans = fac(N) // (fac(K) * fac(N - K))
print(ans)

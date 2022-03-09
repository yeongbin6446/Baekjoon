def prime_list(n : int) -> list: #아라토스테네스의 체
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i,n,i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

M, N = map(int, input().split())

for i in prime_list(N+1):
    if i >= M:
        print(i)



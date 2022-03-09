from sys import stdin

def prime_list(n : int) -> list: #아라토스테네스의 체
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i,n,i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

N = int(stdin.readline())

for i in range(N):
    n = int(stdin.readline())
    ans1, ans2 = 0, 0
    prime = prime_list(n)
    lst = [i for i in prime if i <= n/2]
    lst.reverse()
    for i in lst:
        if n-i in prime:
            print(i, n-i)
            break

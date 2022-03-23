

def fibo(n: int) -> int:
    memo = [[0 for col in range(2)] for row in range(n + 1)]

    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        memo[0] = [1, 0]
        memo[1] = [0, 1]
        for i in range(2, n + 1):
            memo[i][0] = memo[i - 1][0] + memo[i - 2][0]
            memo[i][1] = memo[i - 1][1] + memo[i - 2][1]
        return memo[n]


N = int(input())
for i in range(N):
    n = int(input())
    print(*fibo(n))


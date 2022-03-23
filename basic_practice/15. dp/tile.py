n = int(input())
memo = [0] * (n + 1)
memo[0] = 1
memo[1] = 2
for i in range(2, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

print(memo[n - 1])

import sys

N = int(input())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, N):
    ans += price[i-1] * distance[i-1]

    if price[i-1] < price[i]:
        price[i] = price[i-1]

print(ans)

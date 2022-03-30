N, K = map(int, input().split())
coin = []
for i in range(N):
    val = int(input())
    coin.append(val)

coin.reverse()
count = 0
for i in coin:
    if K / i >= 1:
        count += K // i
        K = K % i

print(count)
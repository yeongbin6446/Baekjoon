N = int(input()) # 로프 수

l = []

for i in range(N):
    l.append(int(input()))

l.sort(reverse=True)
result = []
w = 0

for i, r in enumerate(l):
    result.append(r * (i+1))

print(max(result))





import sys

N, M = map(int, sys.stdin.readline().split())
cords = []
for i in range(N):
    cords.append(int(sys.stdin.readline()))

start = 1
end = max(cords)
cnt = 0
while start <= end:
    result = 0

    mid = (start + end) // 2

    for cord in cords:
        if cord >= mid:
            result += cord // mid

    if result < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1


print(answer)





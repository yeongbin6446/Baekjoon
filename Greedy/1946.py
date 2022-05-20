# 1946. 신입 사원
import sys
t = int(sys.stdin.readline())

for tc in range(t):
    N = int(sys.stdin.readline())
    rank = []
    for i in range(N):
        rank.append(list(map(int,sys.stdin.readline().split())))

    rank.sort()

    c = rank[0][1]
    cnt = 1

    for i in range(1, N):
        if c > rank[i][1]:
            cnt += 1
            c = rank[i][1]

    print(cnt)




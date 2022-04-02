import sys
sys.setrecursionlimit(10000)
T = int(input())

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if ground[x][y] == 1:
        ground[x][y] = 0

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for j in range(K):
        y, x = map(int, input().split())
        ground[x][y] = 1

    result = 0
    for j in range(N):
        for k in range(M):
            if dfs(j,k) == True:
                result += 1
    print(result)




import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False

    if m[x][y] == 1:
        m[x][y] = 0

        dfs(x + 1 , y)
        dfs(x - 1 , y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1 , y + 1)
        dfs(x - 1, y - 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        return True
    return False

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    m = []
    for i in range(M):
        m.append(list(map(int,input().split())))

    result = 0

    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                result += 1

    print(result)
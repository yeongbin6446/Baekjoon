
def dfs(x,y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if m[x][y] == 1:
        global cnt
        cnt += 1
        m[x][y] = 0

        dfs(x - 1,y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

cnt = 0
N = int(input())
num = []
m = []
for i in range(N):
    m.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(N):

        if dfs(i,j) == True:
            num.append(cnt)
            result += 1
            cnt = 0
num.sort()


print(result)
for i in num:
    print(i)
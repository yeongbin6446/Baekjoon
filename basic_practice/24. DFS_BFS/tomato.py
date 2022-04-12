import collections

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if box[nx][ny] == -1:
                continue

            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx,ny])

box = []
N, M = map(int, input().split())

for i in range(M):
    box.append(list(map(int,input().split())))

queue = collections.deque()
dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , 1 , -1]


for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append([i,j])
bfs()
ans = 0
for i in box:
    if 0 in i:
        print(-1)
        exit(0)
    ans = max(ans , max(i))
print(ans - 1)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

N = int(input())     #컴퓨터의 수
M = int(input())     #연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(N+1)]

for i in range(M):
    g1, g2 = map(int,input().split())
    graph[g1].append(g2)
    graph[g2].append(g1)

visited = [False] * (N+1)
dfs(graph,1,visited)

cnt = -1  #1번컴퓨터를 빼고 계산
for i in visited:
    if i == True:
        cnt += 1

print(cnt)
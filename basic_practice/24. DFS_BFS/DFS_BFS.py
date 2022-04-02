import collections

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph:
        if i[0] == v:
            if not visited[i[1]]:
                dfs(graph,i[1],visited)

def bfs(graph, start, visited):
    queue = collections.deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph:
            if i[0] == v:
                if not visited[i[1]]:
                    queue.append(i[1])
                    visited[i[1]] = True

N, M, V = map(int, input().split())
graph = []

for i in range(M):
    g = list(map(int, input().split()))
    graph.append(g)
    g1 = g[::-1]
    graph.append(g1)

graph.sort(key=lambda x : x[1])

visited = [False] * (N+1)
dfs(graph,V,visited)

print()

visited = [False] * (N+1)
bfs(graph,V,visited)

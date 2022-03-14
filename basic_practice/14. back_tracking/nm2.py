N, M = map(int, input().split())
lst = []

def dfs(idx):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(1, N + 1):
            if i > idx:
                lst.append(i)
                dfs(i)
                lst.pop()

dfs(0)

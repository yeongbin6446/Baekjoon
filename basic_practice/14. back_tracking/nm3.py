N, M = map(int, input().split())
lst = []

def dfs():
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(1, N + 1):
            lst.append(i)
            dfs()
            lst.pop()

dfs()


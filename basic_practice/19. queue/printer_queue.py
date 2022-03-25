import collections

for i in range(int(input())):
    order_p = []
    order_i = []
    N, M = map(int, input().split())
    priority = collections.deque(list(map(int,input().split())))
    idx = collections.deque(list(range(N)))

    for j in range(N):
        while priority[0] != max(priority):
            priority.rotate(-1)
            idx.rotate(-1)
        order_p.append(priority.popleft())
        order_i.append(idx.popleft())
    print(order_i.index(M)+1)



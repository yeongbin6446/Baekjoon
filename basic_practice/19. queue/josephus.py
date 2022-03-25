import collections
N, K  = map(int, input().split())
ans = []
queue = collections.deque()

for i in range(1,N+1):
    queue.append(i)

while queue:
    queue.rotate(-(K-1))
    ans.append(queue.popleft())
print('<', end='')

for i in ans:
    if i == ans[-1]:
        print(i, end='')
    else:
        print(i, end=', ')
print('>')

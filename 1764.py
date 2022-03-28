import sys
people = {}
ans = []
N, M = map(int, input().split())
for i in range(N):
    name = sys.stdin.readline().strip()
    people[name] = 'no_listen'

for i in range(M):
    name = sys.stdin.readline().strip()
    if name in people:
        people[name] = 'no_look_listen'
    else:
        people[name] = 'no_look'

for i in people.keys():
    if people[i] == 'no_look_listen':
        ans.append(i)

print(len(ans))
for i in sorted(ans):
    print(i)
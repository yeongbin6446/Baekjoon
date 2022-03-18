lst = []
for i in range(4):
    a, b = map(int,input().split())
    lst.append(b - a)

for i in range(1, len(lst)):
    lst[i] = lst[i] + lst[i-1]

print(max(lst))
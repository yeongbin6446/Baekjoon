import sys

arr = []
big = 0
idx = 0
for i in range(9):
    n = int(sys.stdin.readline())
    arr.append(n)


print(max(arr))
print(arr.index(max(arr))+1)

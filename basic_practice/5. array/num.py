import sys

value = 1
for i in range(3):
    n = int(sys.stdin.readline())
    value = value * n

arr = list(str(value))
count = list(0 for i in range(10))

for i in range(len(count)):
    for j in range(len(arr)):
        if int(arr[j]) == i:
            count[i] += 1

for i in count:
    print(i)


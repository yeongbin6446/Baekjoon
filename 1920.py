import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))
A.sort()
def binary_search(target, data):
    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start+end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

for i in B:
    if binary_search(i,A) == None:
        print(0)
    else:
        print(1)

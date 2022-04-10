from bisect import bisect_left, bisect_right
def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start+end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return None

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cards.sort()
for i in targets:
    if binary_search(i,cards) == None:
        print(0, end =' ')
    else:
        print(bisect_right(cards,i) - bisect_left(cards, i), end=' ')
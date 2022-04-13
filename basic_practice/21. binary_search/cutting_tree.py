def binary_search():
    start = 1
    end = max(trees)
    answer = 0
    while start <= end:
        result = 0
        mid = (start + end) // 2

        for tree in trees:
            if tree > mid:
                result += (tree - mid)

        if result < M:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

N, M = map(int, input().split())

trees = list(map(int,input().split()))

print(binary_search())



import sys

def people(k : int, n : int) -> int:
    p = 0
    down = []
    for i in range(k):
        for j in range(n):
            if i == 0:
                down.append(j+1)
            else:
                if j == 0 :
                    down[j] = 1
                else:
                    down[j] = down[j - 1] + down[j]
    return sum(down)

T = int(sys.stdin.readline())

for i in range (T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(people(k,n))


# 아파트    1호   2호   3호   4호  5호    n
#      3층  1     5     15   35     70   ...
#      2층  1     4     10   20     35   ...
#      1층  1     3     6    10     15   ...
#      0층  1     2     3     4     5    ...
#       k
# k층 (n-1)호 + (k-1)층 n호
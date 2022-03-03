import sys

n = int(sys.stdin.readline())

for i in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    low = 0
    for j in range(score[0]):
        s = sum(score[1:])
        ave = s / score[0]
        if score[1:][j] > ave:
            low += 1
    print(f'{low / score[0] * 100:.3f}%')




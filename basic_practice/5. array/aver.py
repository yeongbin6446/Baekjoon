import sys

n = int(sys.stdin.readline())

score = list(map(int,sys.stdin.readline().split()))

max_score = max(score)
new_score = [0 for i in range(n)]
for i in range(n):
    new_score[i] = (score[i] / max_score) * 100


ave = sum(new_score)/n
print(ave)








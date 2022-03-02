import sys

N, X = map(int,sys.stdin.readline().split())
x = list(map(int,input().split()))

result = []
for i in x:
    if i < X:
        result.append(i)

for i in result:
    print(i, end = ' ')


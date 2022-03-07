import math
A, B, V = map(int,input().split())

day = math.ceil((V-A) / (A-B)) + 1

print(day)

# (V-A)를 (A-B)로 올라가는데 며칠이 걸리는지 계산

A, B, C = map(int,input().split())
if B >= C:
    print(-1)
else:
    X = C - B
    Y = A // X
    print(Y + 1)


N, M = map(int, input().split())
chess = []
for i in range(N):
    wb = input()
    chess.append(wb)
error = 0
for i in range(N):
    if chess[0][0] == 'W':
        if i % 2 == 0 and chess[i][0] == 'B':
            error += 1
        elif i % 2 == 1 and chess[i][0] == 'W':
            error += 1
    else:
        if i % 2 == 0 and chess[i][0] == 'W':
            error += 1
        elif i % 2 == 1 and chess[i][0] == 'B':
            error += 1
    for j in range(1, M-1, 2):
        if chess[i][j] == chess[i][j+1]:
            error += 1

print(error)

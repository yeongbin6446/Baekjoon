from sys import stdin

memo = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def w(a, b, c):
    global memo
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if memo[a][b][c] != 0:
        return memo[a][b][c]
    if a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]
    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]

while True:
    a, b, c = map(int, stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print('w({}, {}, {}) = {}'.format(a, b, c, w(a,b,c)))

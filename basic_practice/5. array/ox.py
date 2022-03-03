import sys

n = int(sys.stdin.readline())
s = 0
value = 0
for i in range(n):
    ox = sys.stdin.readline()
    arr = list(ox)
    for i in arr:
        if i == 'O':
            value += 1
            s += value
        else:
            value = 0
    value = 0
    print(s)
    s = 0






import sys

N = int(sys.stdin.readline())
n = N
i = 0
while True:
    a = int(N/10)
    b = N % 10
    value = str(a + b)
    if len(value) >= 2:
        value = value[1:]
    N = int(str(b) + value)
    i += 1
    if N == n:
        break
print(i)
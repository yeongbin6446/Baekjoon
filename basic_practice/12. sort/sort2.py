from sys import stdin, stdout
N = int(stdin.readline())

lst = []

for i in range(N):
    n = int(stdin.readline())
    lst.append(n)

lst.sort()
for i in lst:
    stdout.write(str(i)+'\n')
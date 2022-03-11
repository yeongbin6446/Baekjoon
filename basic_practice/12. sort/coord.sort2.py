from sys import stdin, stdout
N = int(input())

xy = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    xy.append([y,x])


xy.sort()
for i in xy:
    stdout.write(str(i[1])+' '+str(i[0])+'\n')
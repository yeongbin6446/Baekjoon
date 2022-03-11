from sys import stdin, stdout
N = int(input())

xy = []
for i in range(N):
    x, y = map(int, stdin.readline().split())
    xy.append([x,y])


xy.sort()
for i in xy:
    stdout.write(str(i[0])+' '+str(i[1])+'\n')



n = int(input())

for i in range(1, n+1):
    x, y = map(int,input().split())

    print('Case #{}: {}'.format(i,x+y))
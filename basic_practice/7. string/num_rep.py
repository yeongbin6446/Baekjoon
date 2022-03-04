a = int(input())

for i in range(a):
    N, W = input().split()

    for i in W:
        for j in range(int(N)):
            print(i, end='')
    print()

N = int(input())

cnt = 0
while True:
    if N % 5 == 0:
        print(cnt + N//5)
        break
    cnt += 1
    N -= 3

    if N == 0:
        print(cnt)
        break
    if N < 0:
        print('-1')
        break



T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())

    number = N // H + 1

    floor = N % H

    if floor == 0:
        floor = H
        number = N // H

    if number >= 10:
        number = str(number)
    else:
        number = "0" + str(number)

    floor = str(floor)
    print(floor+number)
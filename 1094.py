X = int(input())
stick = []
length = 64
while True:
    if length > X:
        length = length // 2
    else:
        stick.append(length)
        X = X - length
        length = length // 2
        if X == 0:
            break

print(len(stick))

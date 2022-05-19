
money = int(input())

m = [500, 100, 50, 10, 5, 1]

change = 1000 - money

cnt = 0
for i in m:
    while change >= i:
        change -= i
        cnt += 1
print(cnt)



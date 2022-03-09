while True:
    x, y, z = map(int, input().split())
    if x == 0 and y ==0 and z == 0:
        break
    list = [x ** 2, y ** 2, z ** 2]
    m = max(list)
    list.remove(m)

    if m == sum(list):
        print("right")
    else:
        print("wrong")
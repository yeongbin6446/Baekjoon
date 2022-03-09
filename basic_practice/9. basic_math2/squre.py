x, y, w, h = map(int, input().split())

wx = abs(w-x)
hy = abs(h-y)

if wx > x:
    near_x = x
else:
    near_x = wx

if hy > y:
    near_y = y
else:
    near_y = hy

if near_x > near_y:
    print(near_y)
else:
    print(near_x)
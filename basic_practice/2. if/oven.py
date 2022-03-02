h, m = input().split()
t = input()

h = int(h)
m = int(m)
t = int(t)

if m + t >= 60:
    plus_h = int((m + t) / 60)
    h = h + plus_h
    if h > 23:
        h = h - 24
    m = (m + t) % 60
    print (h, m)
else:
    m = m + t
    print(h, m)



h, m = input().split()

h = int(h)
m = int(m)

if m >= 45:
    m = m - 45
    print(h, m)
else:
    minus_m = 45 - m
    m = 60 - minus_m
    h = h - 1
    if h < 0:
        h = 23
    print(h,m)
first, second, third = map(int,input().split())

if first == second and second == third:
    p = 10000 + first * 1000
elif first == second or second == third or first == third:
    if first == second:
        p = 1000 + first * 100
    elif second == third:
        p = 1000 + second * 100
    else:
        p = 1000 + first * 100
else:
    if first > second:
        if first > third:
            big_num = first
        else:
            big_num = third
    else:
        if second > third:
            big_num = second
        else:
            big_num = third
    p = big_num * 100

print(p)
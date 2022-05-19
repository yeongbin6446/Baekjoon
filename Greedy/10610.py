N = input()

if '0' not in N:
    print(-1)
else:
    s = 0
    for i in range(len(N)):
        s += int(N[i])

    if s % 3 != 0:
        print(-1)
    else:
        sorted_N = sorted(N,reverse=True)
        print(''.join(sorted_N))



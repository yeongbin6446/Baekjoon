case = 1
while True:
    L, P, V = map(int,input().split())

    if L == 0 and P == 0 and V == 0:
        break

    answer = 0

    if V % P >= L:
        A = L
    else:
        A = V % P

    answer  = (V // P) * L + A
    print(f"Case {case}: {answer}")
    case += 1

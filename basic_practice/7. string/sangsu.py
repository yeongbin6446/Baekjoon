A, B = input().split()

A_list = list(A)
B_list = list(B)

A_list.reverse()
B_list.reverse()

A = int(''.join(A_list))
B = int(''.join(B_list))

if A > B:
    print(A)
else:
    print(B)
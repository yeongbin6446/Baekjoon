A, B = map(str,input().split())

A, B = list(A), list(B)
a = ''
b = ''
for i in range(len(A)):
    if A[i] == '5':
        A[i] = '6'
    a += A[i]
for i in range(len(B)):
    if B[i] == '5':
        B[i] = '6'
    b += B[i]

big = int(a) + int(b)
a = ''
b = ''
for i in range(len(A)):
    if A[i] == '6':
        A[i] = '5'
    a += A[i]
for i in range(len(B)):
    if B[i] == '6':
        B[i] = '5'
    b += B[i]

small = int(a) + int(b)

print(small,big)
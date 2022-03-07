A, B = map(int,input().split())
A = str(A)
B = str(B)

list_A = []
list_B = []

if len(A) % 2 == 0:
    for i in range(len(A)):
        if i % 2 == 1:
            list_A.append(A[i - 1] + A[i])
        elif i == len(A) - 1:
            list_A.append(A[i])
else:
    for i in range(len(A)):
        if i == 0:
            list_A.append(A[i])
        if i % 2 == 1:
            list_A.append(A[i] + A[i + 1])

if len(B) % 2 == 0:
    for i in range(len(B)):
        if i % 2 == 1:
            list_B.append(B[i - 1] + B[i])
        elif i == len(B) - 1:
            list_B.append(B[i])
else:
    for i in range(len(B)):
        if i == 0:
            list_B.append(B[i])
        if i % 2 == 1:
            list_B.append(B[i] + B[i+1])        # 입력 받은 숫자 2자리씩 나눔

list_A.reverse()
list_B.reverse()        #역순으로

rest = []
list_sum = []
if len(list_A) >= len(list_B):
    for i in range(len(list_A)):
        for j in range(len(list_B)):
            if i == j:
                s = int(list_A[i]) + int(list_B[j])
                list_sum.append(str(s))  # 각 자리의 합 저장
            else:
                rest.append(list_A[i])
else:
    for i in range(len(list_B)):
        for j in range(len(list_A)):
            if i == j:
                s = int(list_B[i]) + int(list_A[j])
                list_sum.append(str(s))  # 각 자리의 합 저장
            else:
                rest.append(list_B[i])

for i in range(len(list_sum)):
    if len(list_sum[i]) == 3:
        if len(list_sum) == 1:
            rest[0] = str(int(rest[0]) + int(list_sum[i][0]))
            list_sum[i] = list_sum[i][1:]
        else:
            list_sum[i+1] = str(int(list_sum[i+1]) + int(list_sum[i][0]))
            list_sum[i] = list_sum[i][1:]   #각자리의 합이 세자리가 넘어갈경우 그 다음 인덱스의 수와 더함

list_sum.reverse()  #원래대로

ans = ''

rest.reverse()
if len(A) == len(B):
    for i in list_sum:
        ans += i
else:
    for i in rest:
        ans += i
    for i in list_sum:
        ans += i

print(ans)


# 반례 100 100, 9100 900 ......




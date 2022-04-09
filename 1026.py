# solve 1
# N = int(input())
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# A.sort()
# B.sort(reverse=True)
# result = 0
# for i in range(N):
#     result += A[i]*B[i]
#
# print(result)

# solve 2
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
while A:
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))

print(result)
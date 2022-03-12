from sys import stdin, stdout
N = int(stdin.readline())

a = list(map(int,stdin.readline().split()))

result = {}
b = list(set(a))
b.sort()

for i in range(len(b)):
    result[b[i]] = i

for i in a:
    stdout.write(str(result[i])+' ')





















# for i in range(len(b)):
#     cnt = 0
#     for j in range(len(b)):
#         if b[i] != b[j] and b[i]>b[j]:
#             cnt+=1
#     result.append([b[i], cnt])
#
# print(a)
# print(result)
#
# for i in a:
#     for j in result:
#         if i == j[0]:
#             stdout.write(str(j[1])+' ')

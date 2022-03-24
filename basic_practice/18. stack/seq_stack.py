import sys

seq = []
ans = []
j = 1
stack = []
flag = True

for i in range(int(input())):
    n = int(sys.stdin.readline())
    seq.append(n)

while seq:

    while j <= seq[0]:
        stack.append(j)
        ans.append('+')
        j += 1
    if stack[-1] == seq[0]:
        ans.append('-')
        seq.pop(0)
        stack.pop()
    else:
        flag = False
        break

if flag:
    for i in ans:
        print(i)
else:
    print("NO")



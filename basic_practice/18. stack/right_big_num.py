import sys

A = int(input())
seq = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1] * A

stack.append(0)
for i in range(1,A):
        while stack and seq[stack[-1]] < seq[i]:
            ans[stack.pop()] = seq[i]
        stack.append(i)
print(*ans)



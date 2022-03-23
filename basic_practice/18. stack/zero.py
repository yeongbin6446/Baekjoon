import sys
stack = []
for i in range(int(input())):
    K = int(sys.stdin.readline())
    if K == 0:
        stack.pop()
    else:
        stack.append(K)

print(sum(stack))
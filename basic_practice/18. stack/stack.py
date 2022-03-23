import sys
N =int(sys.stdin.readline())
stack = []
for i in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        stack.append(int(command.split()[1]))

    if command == 'pop':
        if not stack:
            print(-1)
            continue
        print(stack.pop())

    if command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    if command == 'top':
        if not stack:
            print(-1)
            continue
        print(stack[-1])

    if command == 'size':
        print(len(stack))


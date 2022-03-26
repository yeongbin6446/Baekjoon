import sys
import collections

deque = collections.deque()

for i in range(int(input())):
    command = sys.stdin.readline().strip()
    if command.split()[0] == 'push_back':
        deque.append(int(command.split()[1]))
    elif command.split()[0] == 'push_front':
        deque.appendleft(int(command.split()[1]))
    elif command == 'pop_front':
        if not deque:
            print(-1)
            continue
        print(deque.popleft())
    elif command == 'pop_back':
        if not deque:
            print(-1)
            continue
        print(deque.pop())
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if not deque:
            print(-1)
            continue
        print(deque[0])
    elif command == 'back':
        if not deque:
            print(-1)
            continue
        print(deque[-1])

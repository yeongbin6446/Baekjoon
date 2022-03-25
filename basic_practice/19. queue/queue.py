import collections
import sys
N =int(sys.stdin.readline())

queue = collections.deque()
for i in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command:
        queue.append(int(command.split()[1]))
    if command == 'pop':
        if not queue:
            sys.stdout.write('-1' + '\n')
            continue
        sys.stdout.write(str(queue.popleft())+'\n')
    if command == 'size':
        sys.stdout.write(str(len(queue))+'\n')
    if command == 'empty':
        if not queue:
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('0'+'\n')
    if command == 'front':
        if not queue:
            sys.stdout.write('-1'+'\n')
        else:
            sys.stdout.write(str(queue[0])+'\n')
    if command == 'back':
        if not queue:
            sys.stdout.write('-1'+'\n')
        else:
            sys.stdout.write(str(queue[-1])+'\n')
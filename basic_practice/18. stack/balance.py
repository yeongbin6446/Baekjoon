from sys import stdin

while True:
    stack = []
    words = stdin.readline().rstrip()
    if words == '.':
        break
    else:
        for i in words:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')' or i == ']':
                if len(stack) == 0:
                    stack = [False]
                    break
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack = [False]
                    break
        if not stack:
            print('yes')
        else:
            print('no')



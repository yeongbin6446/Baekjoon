# import sys
#
# cmds = []
# c = []
# for i in range(int(input())):
#     cmd = sys.stdin.readline().strip()
#     cmds.append(cmd)
#
# if len(cmds) == 1:
#     print(cmds[0])
# else:
#     cmd_compare = cmds[0]
#     for i in range(1,len(cmds)):
#         for j in range(len(cmds[i])):
#             if i == 1:
#                 if cmd_compare[j] == cmds[i][j]:
#                     c.append(cmd_compare[j])
#                 else:
#                     c.append('?')
#             else:
#                 if c[j] != cmds[i][j]:
#                     c[j] = '?'
#
# print(''.join(c))

import sys

cmds = []
c = ''
for i in range(int(input())):
    cmd = sys.stdin.readline().strip()
    cmds.append(cmd)

if len(cmds) == 1:
    print(cmds[0])
else:
    cmd_compare = cmds[0]
    for i in range(1,len(cmds)):
        for j in range(len(cmds[i])):
            if i == 1:
                if cmd_compare[j] == cmds[i][j]:
                    c += cmd_compare[j]
                else:
                    c+='?'
            else:
                if c[j] != cmds[i][j]:
                    c = c.replace(c[j],'?')

print(c)


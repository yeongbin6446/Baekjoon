from sys import stdin

for i in range(int(input())):
    cnt = 0
    ps = stdin.readline().strip()

    for j in ps:
        if cnt == -1:
            break
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
    if cnt == 0:
        print("YES")
    else:
        print("NO")




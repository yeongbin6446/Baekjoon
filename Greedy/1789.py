S = int(input())
cnt = 0
for i in range(1, S+1):
    if S - i >= i or S - i == 0:
        S -= i
        cnt += 1
    if S == 0:
        break

print(cnt)



100
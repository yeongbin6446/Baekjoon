S = input()

S = list(S)

n = S[0]
cnt = [0,0]
cnt[int(n)] += 1
while S:
    if S[0] != n:
        n = S[0]
        cnt[int(n)] += 1
        S.pop(0)
    else:
        S.pop(0)

print(min(cnt))


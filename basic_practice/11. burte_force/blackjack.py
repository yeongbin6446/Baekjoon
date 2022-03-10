N, M = map(int, input().split())
card = list(map(int, input().split()))
s = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(i+2, N):
            if i != j and j != k and i != k:
                s.append(card[i]+card[j]+card[k])
s = set(s)
ans = [i for i in s if M >= i]
print(max(ans))
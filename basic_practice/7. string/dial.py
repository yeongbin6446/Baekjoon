A = input()
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

ans = 0
for a in A:
    for i in alpha:
        if a in i:
            ans += alpha.index(i) + 3
print(ans)

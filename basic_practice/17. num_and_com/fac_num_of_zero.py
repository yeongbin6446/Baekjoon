def fac(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
N = int(input())
f = str(fac(N))
f_list = list(f)
f_list.reverse()

cnt = 0
for i in f_list:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
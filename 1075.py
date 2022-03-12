N = int(input())
F = int(input())


s = str(N)
s = s[:-2]
for i in range(100):
    if i < 10:
        n = '0' + str(i)
        if int(s + n) % F == 0:
            print(n)
            break
    else:
        if int(s + str(i)) % F == 0:
            print(i)
            break

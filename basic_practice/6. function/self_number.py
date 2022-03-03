def func(n:int) -> int:
    s = list(str(n))
    ans = 0
    for i in range(len(s)):
        ans += int(s[i])
    ans += n
    return ans

val = 1
x = []

while True:
    i = func(val)
    val += 1
    if i > 10010:
        break
    x.append(i)

for i in range(1,10001):
    if i not in x:
        print(i)






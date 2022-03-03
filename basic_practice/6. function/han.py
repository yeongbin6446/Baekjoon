import sys

def dist(x : int) -> bool:
    arr = list(str(x))
    temp = []
    for i in range(len(arr) - 1):
        a = int(arr[i])
        b = int(arr[i + 1])
        temp.append(b - a)
    temp = set(temp)
    if len(temp) == 1:
        return True
    else:
        return False

N = int(sys.stdin.readline())
ans = 0
for i in range(1,N+1):
    if dist(i) == True or i < 10:
        ans += 1

print(ans)



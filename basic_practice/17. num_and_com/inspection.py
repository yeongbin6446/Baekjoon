import math
import sys

nums = []
for i in range(int(input())):
    n = int(sys.stdin.readline())
    nums.append(n)

if len(nums) == 2:
    g = abs(nums[1] - nums[0])
else:
    g = abs(nums[1] - nums[0])
    for i in range(2, len(nums)):
        g = math.gcd(g, abs(nums[i] - nums[i - 1]))
ans = []
lg = int((g ** 0.5))
for i in range(2, lg + 1):
    if g % i == 0:
        ans.append(i)
        ans.append(g // i)

ans.append(g)
ans = list(set(ans))
ans.sort()
print(*ans)


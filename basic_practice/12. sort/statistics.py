from sys import stdin
N = int(input())

nums = []
count = [0] * 8001
md = []
for i in range(N):
    n = int(stdin.readline())
    nums.append(n)
    count[n+4000] += 1

m = max(count)
for i, c in enumerate(count):
    if c == m:
        md.append(i-4000)


nums.sort()

mean = round(sum(nums) / len(nums))

median = nums[(N-1)//2]

if len(md) == 1:
    mode = md[0]
else:
    mode = md[1]

ran = max(nums) - min(nums)

print(mean)
print(median)
print(mode)
print(ran)
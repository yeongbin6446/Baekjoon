N = int(input())
factors = list(map(int, input().split()))
if len(factors) == 1:
    ans = factors[0] * factors[0]
else:
    factors.sort()
    ans = factors[0] * factors[(len(factors)-1)]

print(ans)
import math

N = int(input())
ring = list(map(int, input().split()))
for i in range(1,N):
    g = math.gcd(ring[0],ring[i])
    deno = ring[0] // g
    numer = ring[i] // g
    print(f'{deno}/{numer}')



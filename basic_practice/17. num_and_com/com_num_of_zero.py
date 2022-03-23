N, K = map(int, input().split())

def count_number(i, j):
    count = 0
    while i:
        i //= j
        count += i

    return count

n2 = count_number(N,2)
n5 = count_number(N,5)

k2 = count_number(K,2)
k5 = count_number(K,5)

nk2= count_number(N-K,2)
nk5 = count_number(N-K,5)

print(min(n2 - k2 - nk2, n5 - k5 - nk5))
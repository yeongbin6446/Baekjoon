import sys

for i in range(int(input())):
    n1, n2 = map(int, sys.stdin.readline().split())
    big = max(n1,n2)
    small = min(n1,n2)
    while True:
        # 유클리드 호제법으로 최대공약수 구함
        r = big % small
        if r == 0:
            m_fac = small
            break
        big = small
        small = r

    ans = (n1 // m_fac) * (n2 // m_fac) * m_fac
    print(ans)
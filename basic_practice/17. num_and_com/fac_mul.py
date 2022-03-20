import sys

def is_fac_or_mul(n1, n2):
    if n2 % n1 == 0:
        print("factor")
    elif n1 % n2 ==0:
        print("multiple")
    else:
        print("neither")

while True:
    n1, n2 = map(int, sys.stdin.readline().split())
    if n1 == 0 and n2 == 0:
        break
    is_fac_or_mul(n1, n2)
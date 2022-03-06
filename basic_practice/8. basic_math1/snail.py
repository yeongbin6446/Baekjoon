
A, B, V = map(int,input().split())

if V <= A:
    print('0')
elif A-B == 1:
    day = V // (A-B) - A + 1
else:
    day = (V-A) // (A-B) + 2

print(day)


# y = A + (A-B)x #x= 0 1 2 3....
#
#
# # 5 1 6 => 2 : 4 8
# # 6 3 16 => 5 : 3 6 9 12 18      (V-A) <= (A-B)x    10 <= 3*x  x+1   1 <= 4 * x    x=1
# 16 / 6    10   16 3 6 9 12 15
# 12
# 16 / 3
# 5.xxx
# 3 1 8 => 2 4 6 8 4일




n = int(input())

i = 0
ans = 0
x2 = 1

while True:
    x1 = (6 * i)
    x2 = x2 + x1    #각 레벨당 가장 큰수 구함 7 19 37 61

    if n == 1:
        ans = 1
        break
    if n <= x2:     #각 레벨당 가장 큰수보다 n이 작으면
        ans = i + 1 #답 출력
        break
    i+=1

print(ans)

# 규칙 : 각 level당 1개 6개 12개 18개 24개 30개 씩 늘어남
# 같은 level의 방 중 가장 큰 수 7 19 37 61을 이용해 문제해결














n = int(input())

sum = 0
num = 0

while True:     #X를 입력했을 때 X자리 분수의 분자+분모 값을 구함
    num = num + sum
    if n <= num:
        sum = sum
        break
    elif n == 1:
        sum = 2
        break
    sum += 1

ans = n - (num - sum)   #몇번째 순서인지 판별

if n == 1:
    print("1/1")
elif sum % 2 == 0:  #합이 짝수
    print(str(ans) + "/" + str(sum - ans + 1))
else:       #합이 홀수
    print(str(sum - ans + 1) + "/" + str(ans))


# 규칙 : 대각선에 있는 분수의 분자+분모값이 똑같음
# 합이  2 3 4 5 6 7 8 9 10
# 개수  1 3 6 10 15 21 28 36 45

# 숫자를 입력하면 ex) 7  =>  6 < 7 < 10
#                           6 이후 첫번째 값
# 합이 짝수일경우 분자가 최대값부터 시작
# 합이 홀수일결우 분모가 최대값부터 시작

# 그렇다면 1. 개수를 입력하면 분자+분모의 합을 구한다.
#         2. 합이 짝수일 경우 홀수일 경우로 나눠 구현

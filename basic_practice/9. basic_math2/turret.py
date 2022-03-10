from sys import stdin

test_case = int(stdin.readline())

for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int,stdin.readline().split())
    distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    if distance == 0:
        if r1 == r2:    # 똑같은 원인 경우
            print("-1")
        else:    #똑같은 위치에 반지름만 다른 경우
            print("0")
    else:
        if distance == r1 + r2:    #원이 외접하는 경우
            print("1")
        elif distance > r1 + r2:    #겹치는 지점이 없는 경우
            print("0")
        elif distance < r1 + r2:  #하나의 원이 다른 하나의 원의 안에 위치하는 경우
            if abs(abs(r1) - abs(r2)) < distance:        #원이 겹치는 경우
                print("2")
            elif abs(abs(r1) - abs(r2)) == distance:   #원이 내접
                print("1")
            elif abs(abs(r1) - abs(r2)) > distance:   #안에서 겹치는 않는 경우
                print("0")







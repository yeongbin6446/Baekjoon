import collections

def rotate_left(lst, n):
    cnt = 0
    temp = lst.copy()
    while True:
        if temp[0] == n:
            break
        else:
            temp.rotate(-1)
            cnt += 1
    return cnt

def rotate_right(lst, n):
    cnt = 0
    temp = lst.copy()
    while True:
        if temp[0] == n:
            break
        else:
            temp.rotate(1)
            cnt += 1
    return cnt

N, M = map(int,input().split())
lst = collections.deque(list(range(1,N+1)))
location = list(map(int, input().split()))
cnt = 0
for i in location:
    while True:
        if i == lst[0]:
            lst.popleft()
            break
        else:
            if rotate_right(lst, i) > rotate_left(lst, i):
                cnt_l =  rotate_left(lst, i)
                cnt += cnt_l
                lst.rotate(-cnt_l)
            else:
                cnt_r = rotate_right(lst, i)
                cnt += cnt_r
                lst.rotate(cnt_r)

print(cnt)

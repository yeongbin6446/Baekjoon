N = int(input())
meeting = []
for i in range(N):
    start, end = map(int,input().split())
    meeting.append([start,end])

meeting.sort(key = lambda x:(x[1],x[0]))

count = 0
m = 0
for i in meeting:
    if i[0] >= m:
        m = i[1]
        count += 1

print(count)
from sys import stdin, stdout
N = int(stdin.readline())

counting_list = [0] * 10001
for i in range(N):
    n = int(stdin.readline())
    counting_list[n] += 1

for i in range(1,len(counting_list)):
    for j in range(counting_list[i]):
        stdout.write(str(i)+'\n')
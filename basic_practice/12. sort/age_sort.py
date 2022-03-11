from sys import stdin
N = int(stdin.readline())

users = []

for i in range(N):
    age, name = stdin.readline().split()
    age = int(age)
    users.append([age,name])

users.sort(key=lambda x: x[0])
for user in users:
    print(user[0],user[1])
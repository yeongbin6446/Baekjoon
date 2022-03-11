from sys import stdin
N = int(stdin.readline())

words = []
for i in range(N):
    word = stdin.readline().rstrip()
    if [len(word),word] in words:
        continue
    else:
        words.append([len(word), word])

words.sort()

for i in words:
    print(i[1])


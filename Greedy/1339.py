N = int(input())

words = []
for n in range(N):
    words.append(input())

num = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

for word in words:
    for i in range(len(word)):
        num[word[i]] += 10 ** (len(word) - i - 1)

li = []
for value in num.values():
    if value > 0:
      li.append(value)

li.sort(reverse=True)
result = 0
v = 9
for i in range(len(li)):
    result += li[i] * v
    v -= 1

print(result)

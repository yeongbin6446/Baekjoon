N = int(input())

ans = 0
for i in range(N):
    words = input()
    words = list(words)

    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            words[i] = ''

    words.sort()
    a = ''.join(words)

    b = set(words)
    b = list(b)
    b.sort()
    b = ''.join(b)
    if a == b:
        ans += 1

print(ans)


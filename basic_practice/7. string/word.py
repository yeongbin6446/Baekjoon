from collections import Counter

word = input()
word = word.lower()

cnt = Counter(word)

arr = []
for i in cnt.most_common():
    arr.append(i[1])

val = arr.count(max(arr))
if val == 1:
    ans = cnt.most_common(1)[0][0].upper()
    print(ans)
else:
    print('?')




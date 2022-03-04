word = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
    if i in word:
        idx = word.find(i)
        print(idx, end = ' ')
    else:
        print("-1", end = ' ')



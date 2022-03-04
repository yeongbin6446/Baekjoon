words = input()

idx = 0

for i, word in enumerate(words):
    if word == ' ':
        if i == 0 or i == len(words)-1:
            continue
        else:
            idx += 1

if len(words) == 1 and words == ' ':
    num_words = 0
else:
    num_words = idx + 1

print(num_words)

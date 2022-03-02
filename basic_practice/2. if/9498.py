score = input()
score = int(score)

if score < 60:
    print('F')
    exit(0)
if score < 70:
    print('D')
    exit(0)
if score < 80:
    print('C')
    exit(0)
if score < 90:
    print('B')
    exit(0)
if score <= 100:
    print('A')
    exit(0)
else:
    print('F')
    exit(0)
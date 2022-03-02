a = input()
b = input()
a = int(a)
b = int(b)

b1 = b%10
b2 = int((b%100)/10)
b3 = int(b/100)

print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)
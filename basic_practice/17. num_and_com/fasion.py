clothes = {}
clothes_list = []
v = []
for i in range(int(input())):
    clothes = {}
    clothes_list = []
    v = []
    num_clothes = int(input())
    if num_clothes == 0:
        print(0)
        continue
    for j in range(num_clothes):
        c, category = input().split()
        clothes[category] = 0
        clothes_list.append([c, category])

    for k in range(len(clothes_list)):
        if clothes_list[k][1] in clothes:
            clothes[clothes_list[k][1]] += 1

    for n in clothes.values():
        v.append(n)

    ans = 1
    for c in v:
        ans *= (c+1)

    print(ans - 1)


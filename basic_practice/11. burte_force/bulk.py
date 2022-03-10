test_case = int(input())
bulk = []
for i in range(test_case):
    weight, height = map(int,input().split())
    bulk.append([weight, height])

rank = [1] * test_case

for i, b1 in enumerate(bulk):
    for j, b2 in enumerate(bulk):
        if b1 < b2:
            if b1[0] < b2[0] and b1[1] < b2[1]:
                rank[i] += 1

for i in rank:
    print(i,end=' ')




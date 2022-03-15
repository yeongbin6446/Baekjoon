n1, n2 = map(int, input().split())

i = 1

n1_list = []
n2_list = []

while True:
    if n1 % i == 0:
        n1_list.append(i)

    if n2 % i == 0:
        n2_list.append(i)

    if n1 > n2:
        if i == n1:
            break
    else:
        if i == n2:
            break
    i+=1

deno = []
for i in n1_list:
    for j in n2_list:
        if i == j:
            deno.append(i)

m_deno = max(deno)
print(m_deno)

ans = (n1 // m_deno) * (n2 // m_deno) * m_deno
print(ans)



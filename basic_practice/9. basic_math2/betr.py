from sys import stdin, stdout

def prime_list(n : int) -> list: #아라토스테네스의 체
    prime = [True] * n
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i,n,i):
                prime[j] = False

    return [i for i in range(2,n) if prime[i] == True]

while True:
    N = int(stdin.readline())
    if N == 0:
        break
    newlist = list(filter(lambda n : n > N ,prime_list(N*2+1)))   #세는게 아니라 리스트를 잘라내어 리스트의 크기를 출력
    print(len(newlist))


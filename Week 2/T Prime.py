def euler(m, prime):
    p = 2
    while p * p <= m:
        if prime[p]:
            for i in range(p * p, m + 1, p):
                prime[i] = False
        p += 1


n = int(input())
x = [int(i) for i in input().split()]
s = [True] * (10 ** 6 + 1)
euler(10 ** 6, s)
for i in x:
    if i < 4:
        print('NO')
        continue
    elif int(i ** 0.5) ** 2 != i:
        print('NO')
        continue
    if s[int(i ** 0.5)]:
        print('YES')
    else:
        print('NO')

def lcm(x, y):
    m = max(x, y)
    n = min(x, y)
    while m % n:
        m, n = n, m % n
    return int(x * y / n)


def gcd(x, y):
    m = max(x, y)
    n = min(x, y)
    while m % n:
        m, n = n, m % n
    return n


str1 = list(map(int, input().split()))
a = lcm(str1[1], str1[3])
b = int(str1[0] * a / str1[1] + str1[2] * a / str1[3])
print(int(b / gcd(a, b)), int(a / gcd(a, b)), sep='/')

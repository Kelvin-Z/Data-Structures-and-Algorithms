n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
dic = {}
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())
for i in range(n):
    for j in range(n):
        if a[i] + b[j] not in dic:
            dic[a[i] + b[j]] = 0
        dic[a[i] + b[j]] += 1
ans = 0
for i in range(n):
    for j in range(n):
        if - c[i] - d[j] in dic:
            ans += dic[-c[i] - d[j]]
print(ans)
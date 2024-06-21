n = int(input())
ans = []
for i in range(n):
    a, b, c = map(int, input().split())
    T = {}
    for j in range(a):
        u, v = map(int, input().split())
        if u not in T:
            T[u] = [v]
        else:
            T[u].append(v)
    T1 = sorted(T.keys())
    for k in T1:
        T2 = sorted(T[k], reverse=True)
        if len(T[k]) > b:
            c -= sum(T2[0: b])
        else:
            c -= sum(T2)
        if c <= 0:
            ans.append(k)
            break
    if c > 0:
        ans.append('alive')
for i in range(len(ans)):
    print(ans[i])

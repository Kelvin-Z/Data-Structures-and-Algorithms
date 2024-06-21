T = [2, 3, 5, 7]
for i in range(10, 10001):
    j = 0
    for j in range(len(T)):
        if i % T[j] == 0:
            break
    if j == len(T)-1:
        T.append(i)
n = int(input())
for i in range(len(T)):
    m = n - T[i]
    if m in T:
        print(T[i], m)
        break

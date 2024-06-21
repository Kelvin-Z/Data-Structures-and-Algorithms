T = [0, 1, 1]
n = int(input())
if n <= 2:
    print(T[n])
else:
    for i in range(3, n+1):
        T.append(T[i-3] + T[i-2] + T[i-1])
    print(T[n])

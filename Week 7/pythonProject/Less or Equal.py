n, k = map(int, input().split())
data = sorted(list(map(int, input().split())))
if k == n:
    print(data[k-1])
elif k == 0:
    if data[0] != 1:
        print('1')
    else:
        print('-1')
elif data[k-1] < data[k]:
    print(data[k-1])
elif data[k-1] == data[k]:
    print('-1')
for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n):
        ope, num = map(int, input().split())
        if ope == 1:
            arr.append(num)
        elif ope == 2:
            if num == 1:
                arr.pop()
            elif num == 0:
                arr.pop(0)
    if not arr:
        print('NULL')
    else:
        print(' '.join(str(i) for i in arr))

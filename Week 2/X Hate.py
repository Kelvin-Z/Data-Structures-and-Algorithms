for _ in range(int(input())):
    a, b = map(int, input().split())
    s = -1
    A = list(map(lambda x: int(x) % b, input().split()))      # 取余数，大幅减少计算量
    if sum(A) % b:                                            # 若余数之和不能被b整除，则输出数组长度
        print(a)
        continue
    for i in range(a//2+1):
        if A[i] or A[~i]:       # 若余数之和能被b整除，则观察数组头尾取值，若头尾均为0，说明去掉头或尾的数后，数组仍能被b整除，
            s = a-i-1           # 此时观察次头项与次尾项，以此类推，当有一头的数不为0时，说明去掉该数后数组不能被b整除，输出此时数组长度
            break
    print(s)

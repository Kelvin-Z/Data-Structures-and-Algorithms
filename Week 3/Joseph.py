while True:
    num, start, out = input().split()
    num, start, out = int(num), int(start), int(out)
    if num == 0 and start == 0 and out == 0:
        break
    else:
        T = []
        output = []
        start = start - 1            # 从1开始报数
        for i in range(num):
            T.append(i+1)
        for j in range(num):
            for k in range(out):
                if start == len(T):  # 若到达列表最后一个元素，则下一步回到列表第一个元素
                    start = 1
                else:
                    start = start + 1
            output.append(T[start-1])
            del T[start-1]
            start = start - 1         # 列表中少了一个元素
        print(','.join(str(i) for i in output))

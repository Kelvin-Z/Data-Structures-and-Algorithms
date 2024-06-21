def move(num: int, pos_1: str, pos_2: str):
    print('{}:{}->{}'.format(num, pos_1, pos_2))  # 输出


def hanomove(num: int, init: str, final: str, temp: str):  # 含义为借助temp，将num个盘从init移动到final
    if num == 1:
        move(1, init, final)
    else:
        hanomove(num - 1, init, temp, final)  # 首先借助final，将前num-1个盘从init移动到temp
        move(num, init, final)                # 然后将init剩余的一个盘移动到final
        hanomove(num - 1, temp, final, init)  # 再借助init，将num-1个盘从temp移动到final


n, a, b, c = input().split()
hanomove(int(n), a, c, b)

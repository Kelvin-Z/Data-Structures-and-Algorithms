s = input().split()


def cal():
    cur = s.pop(0)
    if cur in '+-*/':
        return str(eval(cal() + cur + cal()))
    else:
        return cur


print('%.6f' % float(cal()))
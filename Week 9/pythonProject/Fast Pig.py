stack = []
min_num = []
while True:
    try:
        s = input().split()
        if s[0] == 'pop':
            if stack:
                stack.pop()
                min_num.pop()
        elif s[0] == 'push':
            stack.append(int(s[1]))
            if len(stack) > 1:
                min_num.append(min(min_num[-1], int(s[1])))
            else:
                min_num.append(int(s[1]))
        elif s[0] == 'min':
            if stack:
                print(min_num[-1])
    except EOFError:
        break
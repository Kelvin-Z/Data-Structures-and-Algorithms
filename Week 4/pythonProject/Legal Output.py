str0 = input()
while 1:
    try:
        str1 = input()
        str_temp = []
        if len(str0) != len(str1):
            print('NO')
        else:
            i = 0
            j = 0
            while 1:
                if not str_temp:
                    if i == len(str0):
                        break
                    str_temp.append(str0[i])
                    i += 1
                if str_temp[-1] != str1[j]:
                    if i == len(str0):
                        break
                    str_temp.append(str0[i])
                    i += 1
                else:
                    j += 1
                    str_temp.pop()
                if j == len(str1):
                    break
            if j == len(str1):
                print('YES')
            else:
                print('NO')
    except EOFError:
        break

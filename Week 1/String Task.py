T = input().lower()
T = T.replace('a', '')
T = T.replace('e', '')
T = T.replace('i', '')
T = T.replace('o', '')
T = T.replace('u', '')
T = T.replace('y', '')
T = '.'.join(T)
print(''.join(['.', T]))

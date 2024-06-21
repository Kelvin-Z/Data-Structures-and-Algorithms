str1 = input()
str2 = str1.split('+')
str3 = ['0']
for i in range(len(str2)):
    str_temp = str2[i].split('n^')
    if str_temp[0] != '0':
        str3.append(str_temp[1])
str4 = map(int, str3)
m = max(str4)
print('n^', m, sep='')

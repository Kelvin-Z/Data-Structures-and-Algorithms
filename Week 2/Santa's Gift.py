str1 = list(map(int, input().split()))
str2 = []
weight = 0
value = 0
for i in range(str1[0]):
    a, b = map(int, input().split())
    str2.append([a, b, a/b])
str2 = sorted(str2, key=(lambda x: x[2]), reverse=True)
for i in range(str1[0]):
    if str1[1] - weight >= str2[i][1]:
        value += str2[i][0]
        weight += str2[i][1]
    else:
        value += (str1[1] - weight) * str2[i][2]
        break
print('%.1f' % value)

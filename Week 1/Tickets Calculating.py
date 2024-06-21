T = input()
T = map(int, T.split())
T_dic = {}
for item_str in T:
    if item_str not in T_dic:
        T_dic[item_str] = 1
    else:
        T_dic[item_str] += 1
m = max(list(T_dic.values()))
out = []
for item_str in T_dic:
    if T_dic[item_str] == m:
        out.append(item_str)
out.sort()
for i in range(len(out)):
    print(out[i], end=' ')

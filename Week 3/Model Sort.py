from collections import defaultdict

n = int(input())
typ_dict = defaultdict(list)
for i in range(n):
    typ, size = map(str, input().split('-'))
    if size[-1] == 'M':                         # 将key值为typ，value值按'M'、'B'分类的元素导入字典
        typ_dict[typ].append((size, float(size[:-1])/1000))   # value为二位列表，便于后续排序
    else:
        typ_dict[typ].append((size, float(size[:-1])))
typ_sort = sorted(typ_dict)                                   # 按key值牌序
for j in typ_sort:
    size_sort = sorted(typ_dict[j], key=lambda x: x[1])       # 按value值排序
    value = ', '.join(k[0] for k in size_sort)
    print('{}: {}'.format(j, value))

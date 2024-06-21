def mid(a: list):                # 计算中位数
    temp = []
    for j in range(len(a)):
        temp.append(a[j])
    temp.sort()
    if len(temp) % 2 == 0:
        return (temp[len(temp)//2-1]+temp[len(temp)//2])/2
    else:
        return temp[len(temp)//2]


n = int(input())
num = 0
distance = [i[1:-1] for i in input().split()]
price = list(map(int, input().split()))
dis_tot = []
for i in range(len(distance)):                    # 计算距离
    distance[i] = distance[i].strip('()')
    distance[i] = list(map(int, distance[i].split(',')))
    dis_tot.append(int(distance[i][0] + distance[i][1]))
ratio = [dis_tot[j]/price[j] for j in range(n)]   # 计算性价比
ratio_mid = mid(ratio)
price_mid = mid(price)
for i in range(n):
    if ratio[i] > ratio_mid and price[i] < price_mid:
        num += 1
print(num)

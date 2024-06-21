n = int(input())
dic = {}
time = list(map(int, (input().split())))         # 记录学生编号及实验时间
for i in range(n):
    dic[i+1] = time[i]
a = sorted(dic.items(), key=lambda x: x[1])      # 按实验时间从小至大排序
student_sort = []
time_sort = []
for i in range(n):
    student_sort.append(a[i][0])
    time_sort.append(a[i][1])
time_wait = 0
for j in range(n-1):
    time_wait += time_sort[j] * (n-j-1) / n       # 计算平均等待时间
print(' '.join(str(k) for k in student_sort))
print('%.2f' % time_wait)

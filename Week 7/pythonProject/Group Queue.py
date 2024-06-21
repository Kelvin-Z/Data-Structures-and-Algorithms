n = int(input())
dic = {}
for i in range(n):
    for j in list(map(int, input().split())):
        dic[j] = i
stack = []
while True:
    ope = input().split()
    if ope[0] == 'ENQUEUE':
        num = int(ope[1])
        if num not in dic:
            stack.append(num)
            dic[num] = num + 100
        else:
            judge2 = False
            for j in range(len(stack)-1, -1, -1):
                if dic[stack[j]] == dic[num]:
                    judge2 = True
                    stack.insert(j + 1, num)
                    break
            if not judge2:
                stack.append(num)
    elif ope[0] == 'DEQUEUE':
        print(stack.pop(0))
    elif ope[0] == 'STOP':
        break
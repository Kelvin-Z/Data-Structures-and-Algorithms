def compare(numbers):
    for k in range(len(numbers)-1):
        if numbers[k+1][:len(numbers[k])] == numbers[k]:
            return 'NO'
    return 'YES'


n = int(input())
for i in range(n):
    numbers = []
    num = int(input())
    for j in range(num):
        numbers.append(input())
    numbers.sort()
    print(compare(numbers))
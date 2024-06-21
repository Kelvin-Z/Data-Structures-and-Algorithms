def update(matrix: list, num: int):  # 在数列尾端新加一个数，记录以该数结尾的最大下降序列元素个数
    matrix.append([num, 1])
    for i in range(len(matrix)-1):
        if matrix[i][0] >= num and matrix[i][1] >= matrix[(len(matrix)-1)][1]:
            matrix[(len(matrix)-1)][1] = matrix[i][1] + 1


n = int(input())
height = list(map(int, input().split()))
T = []
num_seq = []                         # 递推
for j in range(n):
    update(T, height[j])
    num_seq.append(T[j][1])
print(max(num_seq))

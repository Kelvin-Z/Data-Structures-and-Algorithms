class Treenode:
    def __init__(self):
        self.left = None
        self.right = None


def tree_height(node):
    if node is None:
        return -1
    return max(tree_height(node.left), tree_height(node.right))+1


def tree_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return tree_leaves(node.left) + tree_leaves(node.right)


n = int(input())
nodes = [Treenode() for _ in range(n)]
has_parent = [False for _ in range(n)]

for i in range(n):                     # 读取信息
    left_index, right_index = map(int, input().split())
    if left_index != -1:
        nodes[i].left = nodes[left_index]
        has_parent[left_index] = True
    if right_index != -1:
        nodes[i].right = nodes[right_index]
        has_parent[right_index] = True

root_index = has_parent.index(False)   # 寻找根节点
root = nodes[root_index]

height = tree_height(root)
leaves = tree_leaves(root)
print(height, leaves, sep=' ')

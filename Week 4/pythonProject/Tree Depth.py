class Treenode:
    def __init__(self):
        self.left = None
        self.right = None


def tree_depth(node):
    if node is None:
        return 0
    left_depth = tree_depth(node.left)
    right_depth = tree_depth(node.right)
    return max(left_depth, right_depth)+1


n = int(input())
nodes = [Treenode() for _ in range(n)]
for i in range(n):
    left, right = map(int, input().split())
    if left != -1:
        nodes[i].left = nodes[left-1]
    if right != -1:
        nodes[i].right = nodes[right-1]
root = nodes[0]
depth = tree_depth(root)
print(depth)

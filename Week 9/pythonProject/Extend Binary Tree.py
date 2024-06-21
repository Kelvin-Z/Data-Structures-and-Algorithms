class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildtree(s: list):
    if not s[0]:
        return None
    value = s.pop(0)
    if value == '.':
        return None
    root = Treenode(value)
    root.left = buildtree(s)
    root.right = buildtree(s)
    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


s = list(map(str, input().strip()))
root = buildtree(s)
print(''.join(inorder(root)))
print(''.join(postorder(root)))
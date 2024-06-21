class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildtree(s):
    if len(s) == 0:
        return None
    root = Treenode(s[0])
    left = []
    right = []
    for i in range(1, len(s)):
        if s[i] < s[0]:
            left.append(s[i])
        if s[i] > s[0]:
            right.append(s[i])
    root.left = buildtree(left)
    root.right = buildtree(right)
    return root


def post(node: Treenode):
    if not node:
        return []
    out = []
    out.extend(post(node.left))
    out.extend(post(node.right))
    out.append(str(node.value))
    return out


n = int(input())
str0 = list(map(int, input().split()))
print(' '.join(post(buildtree(str0))))

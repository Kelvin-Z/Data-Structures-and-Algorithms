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


def output(root):
    stack = [root]
    out = []
    while stack:
        out.append(str(stack[0].value))
        if stack[0].left:
            stack.append(stack[0].left)
        if stack[0].right:
            stack.append(stack[0].right)
        stack.pop(0)
    return out


str0 = list(map(int, input().split()))
print(' '.join(output(buildtree(str0))))

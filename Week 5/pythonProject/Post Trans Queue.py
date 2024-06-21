class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(s: str):
    stack = []
    for char in s:
        node = Treenode(char)
        if char.isupper():
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack[0]


def output(node: Treenode):
    stack = [node]
    out = []
    while stack:
        if stack[0].left:
            stack.append(stack[0].left)
        if stack[0].right:
            stack.append(stack[0].right)
        out.append(stack.pop(0).value)
    return out


n = int(input())
for i in range(n):
    st = input()
    root = build_tree(st)
    ans = output(root)[::-1]
    print(''.join(ans))

class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildTree(s: str):
    if '1' in s and '0' in s:
        value = 'F'
    elif '1' not in s:
        value = 'B'
    elif '0' not in s:
        value = 'I'
    node = Treenode(value)
    if len(s) > 1:
        s_left = s[:len(s)//2]
        s_right = s[len(s)//2:]
        node.left = buildTree(s_left)
        node.right = buildTree(s_right)
    return node


def post(node):
    if not node:
        return []
    out = []
    out.extend(post(node.left))
    out.extend(post(node.right))
    out.append(node.value)
    return out


n = int(input())
str_input = str(input().strip())
root = buildTree(str_input)
print(''.join(post(root)))
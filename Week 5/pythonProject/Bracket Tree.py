class Treenode:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree(s: str):
    stack = []
    node = None
    for char in s:
        if char.isalpha():
            node = Treenode(char)
            if stack:
                stack[-1].children.append(node)
        elif char == '(':
            if node:
                stack.append(node)
                node = None
        elif char == ')':
            if stack:
                node = stack.pop()
    return node


def preorder(node):
    output = [node.value]
    for child in node.children:
        output.extend(preorder(child))
    return ''.join(output)


def postorder(node):
    output = []
    for child in node.children:
        output.extend(postorder(child))
    output.append(node.value)
    return ''.join(output)


st = input().strip()
st = ''.join(st.split())
root = build_tree(st)
if root:
    print(preorder(root))
    print(postorder(root))

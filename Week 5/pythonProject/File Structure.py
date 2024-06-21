class Treenode:
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []


def figure(node: Treenode):
    graph = [node.name]
    for d in node.dirs:
        subgraph = figure(d)
        graph.extend(['|     ' + sub for sub in subgraph])
    for f in sorted(node.files):
        graph.append(f)
    return graph


n = 0
while True:
    n += 1
    stack = [Treenode('ROOT')]
    while (s := input()) != '*':
        if s == '#':
            exit(0)
        if s[0] == 'd':
            stack.append(Treenode(s))
            stack[-2].dirs.append(stack[-1])
        if s[0] == 'f':
            stack[-1].files.append(s)
        if s[0] == ']':
            stack.pop()
    print('DATA SET {}:'.format(n))
    print(*figure(stack[0]), sep='\n')
    print()

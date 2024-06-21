import heapq


class Node:
    def __init__(self, weight, char=None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.weight == other.weight:
            return self.char < other.char
        return self.weight < other.weight


def buildtree(char_weight_in):
    heap = []
    for char, weight in char_weight_in.items():
        heapq.heappush(heap, Node(weight, char))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight+right.weight, min(left.char, right.char))
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]


def encode_tree(root):
    codes = {}

    def traverse(node, code):
        if node.left is None and node.right is None:
            codes[node.char] = code
        else:
            traverse(node.left, code+'0')
            traverse(node.right, code+'1')
    traverse(root, '')
    return codes


def encode(codes, str_input):
    out = ''
    for char in str_input:
        out += codes[char]
    return out


def decode(root, str_input):
    out = ''
    node = root
    for char in str_input:
        if char == '0':
            node = node.left
        if char == '1':
            node = node.right
        if node.left is None and node.right is None:
            out += node.char
            node = root
    return out


n = int(input())
char_weight = {}
for _ in range(n):
    char_in, weight_in = input().split()
    char_weight[char_in] = int(weight_in)
root_tree = buildtree(char_weight)
codes_tree = encode_tree(root_tree)
while True:
    try:
        str_in = input()
        if str_in[0] in ('0', '1'):
            print(decode(root_tree, str_in))
        else:
            print(encode(codes_tree, str_in))
    except EOFError:
        break

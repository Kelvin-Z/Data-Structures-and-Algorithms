def build_tree(middle: str, pre: str):
    if not pre:
        return []
    root = pre[0]
    output = [root]
    root_index = middle.index(root)
    left_middle = middle[:root_index]
    right_middle = middle[root_index + 1:]
    left_pre = pre[1:len(left_middle) + 1]
    right_pre = pre[len(left_middle) + 1:]
    output = (build_tree(left_middle, left_pre) +
              build_tree(right_middle, right_pre) + output)
    return output


while True:
    try:
        st1 = str(input())
        st2 = str(input())
        print(''.join(build_tree(st2, st1)))
    except EOFError:
        break

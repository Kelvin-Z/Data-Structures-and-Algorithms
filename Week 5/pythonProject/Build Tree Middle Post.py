def build_tree(middle: str, post: str):
    if not post:
        return []
    root = post[-1]
    output = [root]
    root_index = middle.index(root)
    left_middle = middle[:root_index]
    right_middle = middle[root_index + 1:]
    left_post = post[:len(left_middle)]
    right_post = post[len(left_middle):-1]
    output.extend(build_tree(left_middle, left_post))
    output.extend(build_tree(right_middle, right_post))
    return output


st1 = str(input())
st2 = str(input())
print(''.join(build_tree(st1, st2)))

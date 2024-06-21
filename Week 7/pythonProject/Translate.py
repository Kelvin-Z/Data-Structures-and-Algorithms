mem, art = map(int, input().split())
word_list = list(map(int, input().split()))
stack = []
check = 0
for i in range(art):
    word = word_list[i]
    if word not in stack:
        if len(stack) < mem:
            stack.append(word)
        else:
            stack.pop(0)
            stack.append(word)
        check += 1
print(check)
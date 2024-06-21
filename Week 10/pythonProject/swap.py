def swap(a, b):
    a, b = b, a
    # a[0], b[0] = b[0], a[0]


x = [1, 2, 3]
y = [4, 5, 6]
swap(x, y)
print(x, y)
from collections import deque


def find_multiple(n):
    q = deque()
    q.append((1 % n, "1"))
    visited = set([1 % n])

    while q:
        mod, num_str = q.popleft()

        if mod == 0:
            return num_str

        for digit in ["0", "1"]:
            new_num_str = num_str + digit
            new_mod = (mod * 10 + int(digit)) % n

            if new_mod not in visited:
                q.append((new_mod, new_num_str))
                visited.add(new_mod)


while True:
    n = int(input())
    if n == 0:
        break
    print(find_multiple(n))

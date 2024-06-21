s = str(input().strip())

height_old = [0]
height_new = [0]
height_rel = 0
match = [True]
for i in range(len(s)):
    if s[i] == 'd':
        height_old.append(height_old[-1] + 1)
        height_new.append(height_rel + 1)
        height_rel = height_new[-1]
        match.append(False)
    else:
        height_old.append(height_old[-1] - 1)
        for j in range(len(match)-1, -1, -1):
            if not match[j]:
                match[j] = True
                height_rel = height_new[j]
                break

print('{} => {}'.format(max(height_old), max(height_new)))

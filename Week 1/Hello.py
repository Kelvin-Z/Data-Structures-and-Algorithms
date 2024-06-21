T = input()
n = 0
M = list(T)
for i in range(len(M)):
    if M[i] == 'h':
        for j in range(i+1, len(M)):
            if M[j] == 'e':
                for k in range(j+1, len(M)):
                    if M[k] == 'l':
                        for l in range(k+1, len(M)):
                            if M[l] == 'l':
                                for m in range(l+1, len(M)):
                                    if M[m] == 'o':
                                        n = 1
if n == 1:
    print('YES')
else:
    print('NO')

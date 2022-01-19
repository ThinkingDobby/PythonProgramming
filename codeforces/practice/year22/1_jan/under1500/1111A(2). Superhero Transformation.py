s = input()
t = input()
vo = 'aeiou'
flag = False
if len(s) == len(t):
    flag = True
    for i, j in zip(s, t):
        if (i in vo) ^ (j in vo):
            flag = False
            break
print("Yes" if flag else "No")
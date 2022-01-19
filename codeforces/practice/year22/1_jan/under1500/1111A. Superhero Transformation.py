s = list(input())
t = list(input())

vo = {'a', 'e', 'i', 'o', 'u'}

if len(s) != len(t):
    print('No')
else:
    for i in range(len(s)):
        if s[i] in vo:
            s[i] = '*'
        else:
            s[i] = '#'

        if t[i] in vo:
            t[i] = '*'
        else:
            t[i] = '#'
    if "".join(s) == "".join(t):
        print("Yes")
    else:
        print("No")
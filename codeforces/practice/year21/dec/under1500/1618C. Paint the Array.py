import math

for t in range(int(input())):
    input()
    a = list(map(int, input().split(" ")))
    f = a[::2]
    s = a[1::2]
    fgcd = f[0]
    sgcd = s[0]

    for i in range(1, len(f)):
        fgcd = math.gcd(fgcd, f[i])
    for j in range(1, len(s)):
        sgcd = math.gcd(sgcd, s[j])
    if fgcd == sgcd:
        print(0)
        continue
    if fgcd != 1:
        ck = True
        for i in range(len(s)):
            if s[i] % fgcd == 0:
                ck = False
                break
        if ck:
            print(fgcd)
            continue
    if sgcd != 1:
        ck = True
        for i in range(len(f)):
            if f[i] % sgcd == 0:
                ck = False
                break
        if ck:
            print(sgcd)
            continue
    print(0)
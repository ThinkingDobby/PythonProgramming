n = int(input())
if n == 0:
    print(0)
else:
    if (n + 1) % 2 == 0:
        print((n + 1) // 2)
    else:
        print(n + 1)

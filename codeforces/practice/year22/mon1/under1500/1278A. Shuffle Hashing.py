for _ in range(int(input())):
    sp = sorted(input())
    h = input()

    ans = False
    l = len(sp)
    for i in range(0, len(h) - l + 1):
        if sorted(h[i:i + l]) == sp:
            ans = True

    if ans:
        print("YES")
    else:
        print("NO")
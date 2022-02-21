for _ in range(int(input())):
    l, r, k = map(int, input().split())
    if l == r:
        if l == 1:
            print("NO")
        else:
            print("YES")
    else:
        a = l % 2
        b = r % 2
        if a + b == 2:
            if (r - l) // 2 + 1 <= k:
                print("YES")
            else:
                print("NO")
        else:
            if (r - l + 1) // 2 <= k:
                print("YES")
            else:
                print("NO")

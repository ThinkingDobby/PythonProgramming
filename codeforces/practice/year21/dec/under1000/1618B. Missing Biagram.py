for t in range(int(input())):
    c = int(input())
    a = input().split(" ")
    ans = a[0]
    for i in range(1, len(a)):
        if a[i][0] == a[i - 1][1]:
            ans += a[i][1]
        else:
            ans += a[i]
    for i in range(c - len(ans)):
        ans += "a"
    print(ans)
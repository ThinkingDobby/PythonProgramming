for t in range(int(input())):
    a, b, c = map(int, input().split(" "))
    ans = False
    if (b == a and c % 2 == 0) or (b == c and a % 2 == 0) or (a == c and b % 2 == 0):
        ans = True
    l = list(sorted([a, b, c]))
    if l[-1] == l[0] + l[1]:
        ans = True
    print("YES" if ans else "NO")

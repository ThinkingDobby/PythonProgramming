for _ in range(int(input())):
    n, m, r, c = map(int, input().split())
    ans = max([abs(r - i) + abs(c - j) for i, j in [(1, 1), (n, 1), (1, m), (n, m)]])
    print(ans)
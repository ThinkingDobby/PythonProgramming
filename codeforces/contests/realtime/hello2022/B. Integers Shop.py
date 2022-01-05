for _ in range(int(input())):
    n = int(input())
    d = {}
    bl = (10**9 + 1, -1)
    br = (0, -1)
    bad = 10**9 + 1

    for i in range(n):
        l, r, c = map(int, input().split())
        bl = min(bl, (l, c))
        br = max(br, (r, -c))
        d[(l, r)] = min(d.get((l, r), bad), c)  # bad 는 default 값
        print(min(bl[1] - br[1], d.get((bl[0], br[0]), bad)))
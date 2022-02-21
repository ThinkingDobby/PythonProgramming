n, h, a, b, k = map(int, input().split())
for _ in range(k):
    ta, fa, tb, fb = map(int, input().split())
    if ta == tb:
        print(abs(fa - fb))
    else:
        ans = min(abs(fa - a) + abs(fb - a), abs(fa - b) + abs(fb - b)) + abs(ta - tb)
        if fa in range(a, b + 1) and fb in range(a, b + 1):
            ans = min(ans, abs(fa - fb) + abs(ta - tb))
        print(ans)

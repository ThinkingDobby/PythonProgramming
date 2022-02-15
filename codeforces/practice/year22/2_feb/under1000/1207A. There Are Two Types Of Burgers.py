for _ in range(int(input())):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())

    tmp = min(b // 2, p)
    tb = b - tmp * 2
    fc = h * tmp + min(tb // 2, f) * c

    tmp = min(b // 2, f)
    tb = b - tmp * 2
    sc = c * tmp + min(tb // 2, p) * h

    print(max(fc, sc))
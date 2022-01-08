for _ in range(int(input())):
    c, s = map(int, input().split())
    cntr = min(c, s)
    rest = s % cntr
    res = s // cntr

    print((res + 1)**2 * rest + res**2 * (cntr - rest))
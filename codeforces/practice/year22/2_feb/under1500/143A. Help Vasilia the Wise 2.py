r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())


def solve():
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    if i + j == r1 and k + l == r2 and i + k == c1 and j + l == c2 and i + l == d1 and k + j == d2:
                        if len({i, j, k, l}) == 4:
                            print(i, j)
                            print(k, l)
                            return True
    return False


tmp = solve()
if not tmp:
    print(-1)

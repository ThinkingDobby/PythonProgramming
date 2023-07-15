import sys

input = sys.stdin.readline

mod = 998244353

for _ in range(int(input())):
    n, m, k, q = map(int, input().split())

    xs = set()
    ys = set()

    data = [list(map(int, input().split())) for _ in range(q)][::-1]

    cnt = 0
    for i in range(q):
        x, y = data[i]
        if len(xs) >= n or len(ys) >= m or (x in xs and y in ys):
            continue
        xs.add(x)
        ys.add(y)
        cnt += 1

    print(pow(k, cnt, mod))

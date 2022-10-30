import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    x = set()
    y = set()

    for _ in range(m):
        a, b = map(int, input().split())
        x.add(a)
        y.add(b)

    print("YES" if len(x) < n and len(y) < n else "NO")

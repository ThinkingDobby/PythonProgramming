import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ta = set([i for i in a if i <= k])
    tb = set([i for i in b if i <= k])

    if ta | tb == set([i for i in range(1, k + 1)]) and len(ta) >= k // 2 and len(tb) >= k // 2:
        print("YES")
    else:
        print("NO")
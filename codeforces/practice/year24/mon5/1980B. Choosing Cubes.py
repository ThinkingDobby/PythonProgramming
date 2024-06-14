import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))

    memo = [i for i in a if i >= a[f - 1]]
    if len(memo) - 1 < k:
        print("YES")
    else:
        if len(memo) - a.count(a[f - 1]) < k:
            print("MAYBE")
        else:
            print("NO")

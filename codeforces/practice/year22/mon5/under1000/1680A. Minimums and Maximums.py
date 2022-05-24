import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())

    if set(range(l1, r1 + 1)) & set(range(l2, r2 + 1)):
        print(max(l1, l2))
    else:
        print(l1 + l2)

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    tmp = set([b[i] - a[i] for i in range(n)]) - {0, 1}

    print("YES" if len(tmp) == 0 else "NO")


import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        print(abs(a[i]) if i % 2 == 0 else -abs(a[i]), end=' ')
    print()
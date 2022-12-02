import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    f = sorted(data)[-1]
    s = sorted(data)[-2]

    for i in data:
        print(i - f if i != f else i - s, end=' ')
    print()
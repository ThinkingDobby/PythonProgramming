import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    sdata = sorted(data[1:])

    now = data[0]
    for i in sdata:
        if i > now:
            now = (now + i + 1) // 2

    print(now)

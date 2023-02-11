import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = input().rstrip()

    s = 0
    e = n - 1

    while s < e:
        if {data[s], data[e]} != {'0', '1'}:
            break
        s += 1
        e -= 1

    print(e - s + 1)
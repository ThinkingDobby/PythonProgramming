import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    if b * c == a * d:
        print(0)
    else:
        t_min = min(b * c, a * d)
        t_max = max(b * c, a * d)
        if t_min == 0 or t_max % t_min == 0:
            print(1)
        else:
            print(2)
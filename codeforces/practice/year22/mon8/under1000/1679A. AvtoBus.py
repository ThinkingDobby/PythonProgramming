import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    value = n // 6
    rest = n % 6
    if rest < 4 and value > 0 and rest != 0:
        rest += 6
        value -= 1

    if rest not in [0, 4, 8]:
        print(-1)
    else:
        min_v = value + rest // 4
        tmp = value
        max_v = tmp // 2 * 3 + tmp % 2 + rest // 4
        print(min_v, max_v)

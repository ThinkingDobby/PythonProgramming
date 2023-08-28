import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(input().rstrip())

    if k % 2 == 0:
        print(''.join(sorted(data)))
    else:
        evens = sorted([data[i] for i in range(n) if i % 2 == 0])
        odds = sorted([data[i] for i in range(n) if i % 2 == 1])

        oi = ei = 0
        for i in range(n):
            if i % 2 == 0:
                print(evens[ei], end='')
                ei += 1
            else:
                print(odds[oi], end='')
                oi += 1
        print()



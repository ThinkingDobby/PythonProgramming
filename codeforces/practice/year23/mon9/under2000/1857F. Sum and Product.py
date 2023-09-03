import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = collections.Counter(map(int, input().split()))

    for _ in range(int(input())):
        x, y = map(int, input().split())

        cnt = 0
        rev = x < 0
        for i in sorted(data, reverse=rev):
            if rev:
                if i < x // 2:
                    break
            else:
                if i > x // 2:
                    break

            if x - i in data and i * (x - i) == y:
                if i == x - i:
                    cnt += data[i] * (data[i] - 1) // 2
                else:
                    cnt += data[i] * data[x - i]

        print(cnt, end=' ')
    print()

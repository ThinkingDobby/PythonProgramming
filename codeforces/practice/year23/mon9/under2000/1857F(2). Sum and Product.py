import collections
import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = collections.Counter(map(int, input().split()))

    for _ in range(int(input())):
        b, c = map(int, input().split())

        tmp = b**2 - 4 * c

        cnt = 0
        if tmp > 0:
            fv = (b + math.sqrt(tmp)) / 2
            sv = (b - math.sqrt(tmp)) / 2

            if fv % 1 == 0 and sv % 1 == 0:
                fv = int(fv)
                sv = int(sv)

                if fv in data and sv in data:
                    cnt += data[fv] * data[sv]
        elif tmp == 0:
            v = b / 2
            if v % 1 == 0:
                v = int(v)

                if v in data:
                    cnt += data[v] * (data[v] - 1) // 2

        print(cnt, end=' ')
    print()
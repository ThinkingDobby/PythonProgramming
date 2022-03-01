import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = [math.inf] + list(map(int, input().split()))

    for i in range(1, n):
        if data[i] < data[i + 1]:
            while True:
                check = True
                for j in range(i, -1, -1):
                    if data[j] != data[i + 1]:
                        check = False
                    if data[j] >= data[i + 1] or data[j] > data[j + 1]:
                        break
                    if data[j - 1] >= data[j]:
                        tmp = min(data[j - 1] + 1, data[j + 1]) - data[j]
                        k -= tmp
                        data[j] += tmp
                        if k <= 0:
                            check = True
                            print(j)
                            break
                if check:
                    break
        if k <= 0:
            break

    if k > 0:
        print(-1)
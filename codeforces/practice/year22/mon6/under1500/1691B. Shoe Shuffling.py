import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = dict(collections.Counter(map(int, input().split())))

    if min(list(data.values())) > 1:
        last = 1
        for i in data.keys():
            print(last + data[i] - 1, end=' ')
            for j in range(last, last + data[i] - 1):
                print(j, end=' ')
            last = last + data[i]
        print()
    else:
        print(-1)

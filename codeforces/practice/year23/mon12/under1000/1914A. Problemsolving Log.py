import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = collections.Counter(input().rstrip())

    cnt = 0
    for i in data:
        if ord(i) - 64 <= data[i]:
            cnt += 1

    print(cnt)

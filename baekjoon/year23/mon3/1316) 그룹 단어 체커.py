import collections
import sys

input = sys.stdin.readline

cnt = 0

for _ in range(int(input())):
    data = list(input().rstrip())
    n = len(data)

    data = data + ['0']
    chk = collections.defaultdict(int)

    ans = True
    for i in range(n):
        if data[i] != data[i + 1]:
            chk[data[i]] += 1
            if chk[data[i]] > 1:
                ans = False
                break

    cnt += 1 if ans else 0

print(cnt)
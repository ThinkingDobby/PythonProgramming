import itertools
import sys

input = sys.stdin.readline

pw = input().rstrip()
data = [input().rstrip() for _ in range(int(input()))]

memo = list(map(lambda x: x[0] + x[1], itertools.permutations(data * 2, 2)))

ans = False
for i in memo:
    if pw in i:
        ans = True
        break

print("YES" if ans else "NO")

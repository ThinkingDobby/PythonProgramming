import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    counter = collections.Counter(data)
    memo = [i for i in counter.items() if i[1] >= 3]
    if len(memo) == 0:
        print(-1)
    else:
        print(memo[0][0])
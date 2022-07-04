import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

memo = [i for i in data if i % 2 == 0]
if len(memo) != 0 and len(memo) != n:
    print(*sorted(data))
else:
    print(*data)
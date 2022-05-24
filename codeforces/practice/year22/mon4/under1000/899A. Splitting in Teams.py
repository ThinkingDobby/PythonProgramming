import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
mv = min(data.count(1), data.count(2))
print(mv + max(0, (data.count(1) - mv) // 3))
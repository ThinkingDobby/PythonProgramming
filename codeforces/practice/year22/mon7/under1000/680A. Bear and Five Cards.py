import sys

input = sys.stdin.readline

data = list(map(int, input().split()))
tmp = [i * min(data.count(i), 3) for i in set(data) if 2 <= data.count(i)]
print(sum(data) - (max(tmp) if tmp else 0))
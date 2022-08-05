import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
tmp = sorted(data)
print(tmp[1] if len(tmp) > 1 else "NO")
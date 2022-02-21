import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
s = list(map(int, input().split()))
b = list(map(int, input().split()))

tmp = r // min(s)
print(max(max(b) * tmp + r % min(s), r))

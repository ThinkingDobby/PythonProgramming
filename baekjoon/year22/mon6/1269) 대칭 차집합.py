import sys

input = sys.stdin.readline

n, m = map(int, input().split())
f = set(map(int, input().split()))
s = set(map(int, input().split()))
print(n + m - len(f & s) * 2)
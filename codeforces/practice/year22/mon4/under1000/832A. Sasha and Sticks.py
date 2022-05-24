import sys

input = sys.stdin.readline

n, k = map(int, input().split())
tmp = n // k
print("YES" if tmp % 2 == 1 else "NO")
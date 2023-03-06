import sys

input = sys.stdin.readline

n = int(input())

a = sum(map(int, input().split()))
b = sorted(map(int, input().split()))

print("YES" if a <= b[-1] + b[-2] else "NO")
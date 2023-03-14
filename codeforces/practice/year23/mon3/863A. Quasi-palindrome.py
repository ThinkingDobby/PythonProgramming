import sys

input = sys.stdin.readline

data = input().rstrip().rstrip('0')

print("YES" if data == data[::-1] else "NO")
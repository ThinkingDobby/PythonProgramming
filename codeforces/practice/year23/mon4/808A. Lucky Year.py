import sys

input = sys.stdin.readline

n = list(input().rstrip())

print(int(str(int(n[0]) + 1) + '0' * (len(n) - 1)) - int(''.join(n)))
import sys

input = sys.stdin.readline

n = int(input())

print(n // 7 * 2 + max(n % 7 - 5, 0), n // 7 * 2 + min(n % 7, 2))
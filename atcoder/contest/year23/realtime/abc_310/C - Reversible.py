import sys

input = sys.stdin.readline

n = int(input())

memo = set()
for i in range(n):
    s = input().rstrip()
    sr = s[::-1]

    memo.add(min(s, sr))

print(len(memo))
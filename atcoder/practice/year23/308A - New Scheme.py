import sys

input = sys.stdin.readline

s = list(map(int, input().split()))

ans = False
if s == sorted(s):
    if 100 <= s[0] <= 675 and 100 <= s[-1] <= 675:
        if all([i % 25 == 0 for i in s]):
            ans = True

print("Yes" if ans else "No")
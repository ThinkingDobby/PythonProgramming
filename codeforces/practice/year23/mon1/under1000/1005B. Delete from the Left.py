import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

chk = -1
for i in range(min(len(s), len(t))):
    if s[len(s) - i - 1] != t[len(t) - i - 1]:
        chk = i
        break

print(max(len(s), len(t)) - min(len(s), len(t)) if chk == -1 else len(s) - chk + len(t) - chk)

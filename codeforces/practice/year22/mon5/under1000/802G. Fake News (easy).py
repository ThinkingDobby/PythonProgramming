import sys

input = sys.stdin.readline

chk = ['h', 'e', 'i', 'd', 'i']
idx = 0

for i in input().rstrip():
    if i == chk[idx]:
        idx += 1
        if idx == 5:
            break

print("YES" if idx == 5 else "NO")
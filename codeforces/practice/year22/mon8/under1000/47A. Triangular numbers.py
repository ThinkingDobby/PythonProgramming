import sys

input = sys.stdin.readline

ans = []
for i in range(100):
    tmp = i * (i + 1) // 2
    ans.append(tmp)
    if tmp > 500:
        break

print("YES" if int(input()) in ans else "NO")

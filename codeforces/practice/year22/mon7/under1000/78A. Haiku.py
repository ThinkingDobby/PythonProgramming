import sys

input = sys.stdin.readline

ans = []
for _ in range(3):
    cnt = 0
    data = input().rstrip()
    for i in data:
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    ans.append(cnt)

if ans == [5, 7, 5]:
    print("YES")
else:
    print("NO")
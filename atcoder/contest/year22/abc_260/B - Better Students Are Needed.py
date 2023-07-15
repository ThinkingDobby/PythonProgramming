import sys

input = sys.stdin.readline

n, x, y, z = map(int, input().split())

f = list(map(int, input().split()))
s = list(map(int, input().split()))
math = sorted(zip(f, list(range(0, n))), key=lambda x: (-x[0], x[1]))
eng = sorted(zip(s, list(range(0, n))),key=lambda x: (-x[0], x[1]))
tot = sorted(zip([f[i] + s[i] for i in range(n)], list(range(0, n))), key=lambda x: (-x[0], x[1]))

ans = set()

cnt = 0
for i in range(n):
    if cnt >= x:
        break
    if math[i][1] not in ans:
        ans.add(math[i][1])
        cnt += 1

cnt = 0
for i in range(n):
    if cnt >= y:
        break
    if eng[i][1] not in ans:
        ans.add(eng[i][1])
        cnt += 1

cnt = 0
for i in range(n):
    if cnt >= z:
        break
    if tot[i][1] not in ans:
        ans.add(tot[i][1])
        cnt += 1

for i in sorted(ans):
    print(i + 1)
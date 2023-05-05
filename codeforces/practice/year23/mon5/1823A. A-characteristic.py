import sys

input = sys.stdin.readline

chk = [0] * 101
for i in range(1, 101):
    chk[i] += chk[i - 1] + i
print(chk)

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = False
    for i in range(101):
        if chk[i] == k:
            ans = True
            print("YES")
            print(*([1] * (i + 1) + [-1] * (k - (i + 1))))
            break
    if not ans:
        print("NO")
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    ans = []
    for i in range(n // 2):
        ans.append(i + 1)
        ans.append(n - i)

    if n % 2 == 1:
        ans.append(n // 2 + 1)

    print(*ans)
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, k = map(int, input().split())

    ans = -1
    for i in range(max(x, k), x + 2 * k):
        if sum([int(j) for j in str(i)]) % k == 0:
            ans = i
            break

    print(ans)
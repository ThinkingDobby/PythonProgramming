import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = input().rstrip()

    cnt = 0
    for i in range((n + 1) // 2 - 1):
        if data[i] == data[n - 1 - i]:
            cnt += 1
        else:
            break

    print("YES" if cnt >= k else "NO")
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = set(map(int, input().split()))

    ans = False
    for i in list(data):
        if k + i in data:
            ans = True
            break

    print("YES" if ans else "NO")